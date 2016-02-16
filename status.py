import sys
import datetime
from time import sleep
#import music
import subprocess
import re
import os

DEFAULT_MPC_FMT = "[[%artist% - ]%title%[ (on %album%)]]|[%file%]"

# A script to pipe into dzen

#for piping out too
NULL = open("/dev/null")

# for unicode
import codecs, locale

def debug(line, nn=False):
        sys.stderr.write(str(line)+"\n" if not nn else str(line))
        sys.stderr.flush()

def humanize_bytes(num, round_to=1):
        mappings = ["b", "kib", "mib", "gib", "tib", "pib"]
        num = float(num)
        count = 0
        while num > 1024:
                num /= 1024
                count += 1
        return round(num, round_to), mappings[count]

#set to a unicode enabled pipe
debug(locale.getpreferredencoding())
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

class RunningLoop(object):

        def __init__(self, interval=0.2):
                self.interval = interval
                self.func_list = []

        def display(self, func):

                self.func_list.append(func)
                if not hasattr(func, 'every'):
                        func.every = 1
                return func

        def display_const(self, some_string, every=1):
                func = lambda: some_string
                func.every = every
                self.func_list.append(func)

        def apply(self, func_tuple):
                func, wait, last_out = func_tuple
                if wait >= func.every:
                        try:
                                out = unicode(func())
                        except Exception, e:
                                debug(func.__name__+' '+str(e))
                                out = u''
                        return (func, 0, out)
                else:
                        return (func, wait+self.interval, last_out)

        def run(self):

                func_tuples = zip(self.func_list,
                                  [x.every for x in self.func_list],
                                  ('',)*len(self.func_list))
                while True:
                        func_tuples = map(self.apply, func_tuples)
                        s = "".join(map(lambda (f, w, l): l, func_tuples))
                        subprocess.call(["xsetroot", "-name", s])

                        sleep(self.interval)

runner = RunningLoop()

# DATE

@runner.display
def date():
        return datetime.datetime.now().strftime("%A, %d-%m-%Y %I:%M")
date.every = 0.9

runner.display_const(" <> ") # Volume/Now Playing

@runner.display
def volume():
        data = subprocess.check_output(["amixer", "get", "Master"])
        level = re.search(r"Mono: [^\[]*\[([0-9%]*)\]", data).group(1)
        return level
volume.every = 0.3

runner.display_const(" <> ")

#@runner.display
def now_playing():
    mpc_format_arg = ["-f", os.environ.get("MPC_FMT", DEFAULT_MPC_FMT)]
    mpc_status = subprocess.check_output(["mpc"] + mpc_format_arg).split("\n")
    if len(mpc_status) < 3:
        return ""
    return mpc_status[0].decode('utf-8')

#runner.display_const(" <> ") # Network

#@runner.display
#def ip_data():
#        external_ip = subprocess.check_output(["curl", "--silent", 
#                                               "http://icanhazip.com"])
#        external_ip = external_ip.strip()
#        internal_ip = subprocess.check_output(["ip", "addr", "show", "eth0"])
#        internal_ip = re.search(r"inet ([0-9.]*)", internal_ip).group(1)
#        debug("Updating Network Info..")
#        return ("E: {external} I: {internal}")\
#                .format(internal=internal_ip, external=external_ip)
#
#ip_data.every = 500

@runner.display
def battery():
    res = subprocess.check_output(["acpi"])
    level = re.search(r"([0-9]+%)", res).group(1)
    return "Batt: " + level

runner.display_const(" <> ")

#@runner.display
#def network_status():
#        try:
#                # ping google to check the network
#                subprocess.check_call(["ping", "-w 1", "-c 1", "google.com"],
#                                                          stdout=NULL)
#                return "Up"
#        except subprocess.CalledProcessError:
#                return "Down"
#
#network_status.every = 30
#
#runner.display_const(" ")

@runner.display
def network_usage():
        f = open("/proc/net/dev")
        stats = f.read()
        f.close()

        eth = re.search(r"wlan0:(.*)$", stats, flags = re.MULTILINE)
        if eth is not None: eth = eth.group(1)
        else: return ""
        eth = eth.strip()
        eth = re.split(r"\s*", eth)
        recv = humanize_bytes(int(eth[0]))
        sent = humanize_bytes(int(eth[8]))
        return ("S: {sent[0]}{sent[1]} R: {recv[0]}{recv[1]}")\
                   .format(sent=sent, recv=recv)

runner.run()
