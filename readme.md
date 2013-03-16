My ~/bin/ files
=========

### Scripts I Wrote
* ashuffle - A script that will continuously enque songs for [mpd][].
* dotmake - A script that generates a Makefile to link your dotfiles automatically.
* lf - A simple bash script that list files in a directory based on size.
* linkdf.sh - It's a simple script to symbolically link my dot files from a
directory into ~. It could use some fixing up.
* mpcp - an extremely minimal music mpd interface using mpc
* music.py - It's an interface to all of the music players I was using at the
time: Spotify (the linux version) and cmus. It provides a standard interface to
do things like playing, pausing and getting information about playing tracks.
* music\_bindings - It's the cli interface to music.py. I don't thing it's ever
worked.
* nfsn-pingbot - A script I cron to update my ip address on 
[NearlyFreeSpeach.net][nfsn]'s
DNS. It's there to provide dynamic DNS stuff.
* nfsn.py - A [requests][] auth plugin thing for the [NFSN][nfsn] api.
* opml2feeds - Converts a .opml file of podcasts to yaml compatible with [podcasts][].
* pick - output random lines from stdin, using probability!
* psearch - A script that greps your PATH for programs.
* remounte - One of my drives keeps disconnecting. So instead of fixing the problem I 
wrote a script to disconnect it and reconnect it.
* rundzen - Pipes status.py into [dzen2][] with some custom font options.
* status.py - A python script that writes various system information to stdout
in [dzen2][]'s format for display. The top of it actually has a class for adding in
arbitrary information. It's actually kinda cool.
* updatesums - Update a checksums file
* watcher - A script that runs some command when a file (or directory of files) 
updates by using inotify. Handy for doing things like re-compiling files.
* win-remote - A shortcut for connecting to my school's windows machines.

### Scripts I Didn't Write
* dbox - It's a cli for drop box, I'm pretty sure it's official, but
I don't remember.
* todo - Gina Trapani's [todo.txt-cli][todo].
* [youtube-dl][] - The every video downloader.

### Symbolic Links
* [podcasts][]
* [soundrip][]

  [podcasts]: https://github.com/Joshkunz/podcasts
  [soundrip]: https://github.com/Joshkunz/soundrip
  [dzen2]: https://github.com/robm/dzen
  [nfsn]: https://www.nearlyfreespeech.net/
  [requests]: http://docs.python-requests.org/en/latest/
  [youtube-dl]: http://rg3.github.com/youtube-dl/
  [todo]: http://todotxt.com/
  [mpd]: http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki
