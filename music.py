"""
Grand Unified Music controller for python.
"""

import dbus, subprocess
bus = dbus.SessionBus()

class Spotify(object):

	def __init__(self):
		self.spotify = bus.get_object("org.mpris.MediaPlayer2.spotify",
									  "/org/mpris/MediaPlayer2")
		self.getset = dbus.Interface(self.spotify,
									 "org.freedesktop.DBus.Properties")
	
	def play(self):
		if self.PlaybackStatus != "Playing":
			self.spotify.PlayPause()

	def pause(self):
		self.spotify.Pause()

	def next(self):
		self.spotify.Next()
	
	def back(self):
		self.spotify.Previous()

	def toggle(self):
		self.spotify.PlayPause()
	
	def __getattr__(self, name):
		return self.getset.Get("org.mpris.MediaPlayer2.Player", name)

	def meta(self):
		data = self.Metadata
		updated = {}
		for x in data.keys():
			n = x.split(":")[1]
			updated[n] = data[x]
		return updated


class Cmus(object):

	def run(self, command, output=False):
		if output:
			return subprocess.check_output(command)
		else:
			return subprocess.call(command)

	def play(self):
		self.run(["cmus-remote", "--play"])
	
	def pause(self):
		self.run(["cmus-remote", "--pause"])

	def toggle(self):
		self.pause()

	def next(self):
		self.run(["cmus-remote", "--prev"])
	
	def back(self):
		self.run(["cmus-remote", "--next"])

	def meta(self):
		props = {}
		props["tag"] = {}
		props["set"] = {}
		settings = self.run(["cmus-remote", "-Q"],
							output=True)
		for l in settings.split("\n"):
			lsplit = l.split(' ')
			if lsplit[0] in ["tag", "set"]:
				props[lsplit[0]][lsplit[1]] = ' '.join(lsplit[2:])
			elif l:
				props[lsplit[0]] = ' '.join(lsplit[1:])
		return props

def getPlayer():
	try:
		return Spotify()
	except dbus.exceptions.DBusException:
		return Cmus()

