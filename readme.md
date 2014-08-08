My ~/bin/ files
=========

### Scripts I Wrote
* ashuffle - A script that will continuously enque songs for [mpd][].
* dotmake - A script that generates a Makefile to link your dotfiles automatically.
* finish\_album - Add the tracks from the currently playing song's album
  after the currently playing song. 
* flac2mp3 - Simple script for converting a directory full of flac files into
  a directory full of mp3 files.
* fpost - My school's CMS [Canvas](http://www.instructure.com/) has a pretty awful
  WYSIWYG editor. Since I post a lot of example source, I wrote this script
  which renders markdown files, inlines the CSS and then dumps the HTML to
  standard out for pasting into the bare-HTML input.
* htmlencode - Encode a given string into HTML encoded identities.
* inlinebody - Takes an HTML page on stdin, inlines the CSS and outputs
  the 'body' portion. Used with `fpost`.
* lf - A simple bash script that list files in a directory based on size.
* linkdf.sh - It's a simple script to symbolically link my dot files from a
  directory into ~. It could use some fixing up.
* mpcp - an extremely minimal music mpd interface using mpc
* mpc_trans - A bash script for transferring the state of one MPD instance to
  another mpd instance.
* mqueue - Adds a file to mpd, even if that file isn't in MPD's library. I
  had to [patch][fileaccess-patch] mpd to get this to work. I think it had
  a faulty check.
* mshuffle_dir - Shuffle add music files in this directory and all sub-directories
  using [ashuffle][].
* music.py - It's an interface to all of the music players I was using at the
  time: Spotify (the linux version) and cmus. It provides a standard interface to
  do things like playing, pausing and getting information about playing tracks.
* music\_bindings - It's the cli interface to music.py. I don't thing it's ever
  worked.
* nfsn-pingbot - A script I cron to update my ip address on 
  [NearlyFreeSpeach.net][nfsn]'s
  DNS. It's there to provide dynamic DNS stuff.
* opml2feeds - Converts a .opml file of podcasts to yaml compatible with [podcasts][].
* pdf2kindle - A python script that takes a pdf, converts it to a mobile-formatted
  pdf (using [k2pdfopt][]) and then mails that PDF to your kindle email address
  so it get synced onto your kindle. I primarily use this for reading academic
  papers on my kindle. NOTE: The output pdf is formatted specifically for the
  kindle paperwhite. If you use it with a different model, you'll want to change
  the options supplied to [k2pdfopt][] (see the `convert` function).
* pfile - Open the next file of a given name, if that file already exists, add an
  incrementing counter to the end.
* pick - output random lines from stdin, using probability!
* psearch - A script that greps your PATH for programs.
* remounte - One of my drives keeps disconnecting. So instead of fixing the problem I 
  wrote a script to disconnect it and reconnect it.
* rip - A script that rips a CD using abcde. This script exists because I kept
  forgetting what options I wanted to specify.
* rundzen - Pipes status.py into [dzen2][] with some custom font options.
* shuff - Runs [ashuffle][] with some common options.
* status.py - A python script that writes various system information to stdout
  in [dzen2][]'s format for display. The top of it actually has a class for adding in
  arbitrary information. It's actually kinda cool.
* strip_audio - BASH script for removing audio from video track.
* sync\_music - Sync my music library between my laptop and my desktop.
* sync\_musicr - Sync my music library between my laptop and my remote server.
* tn - A simple command to open a new not taking file.
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
* [ashuffle][]
* [k2pdfopt][]
* python27 - Symlinks to my local install of python 2.7 for cross-compatibility.
* [vlcwrap][]
* [qmv][]

  [podcasts]: https://github.com/Joshkunz/podcasts
  [soundrip]: https://github.com/Joshkunz/soundrip
  [ashuffle]: https://github.com/Joshkunz/ashuffle
  [dzen2]: https://github.com/robm/dzen
  [nfsn]: https://www.nearlyfreespeech.net/
  [requests]: http://docs.python-requests.org/en/latest/
  [youtube-dl]: http://rg3.github.com/youtube-dl/
  [todo]: http://todotxt.com/
  [mpd]: http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki
  [k2pdfopt]: http://willus.com/k2pdfopt/
  [fileaccess-patch]: https://gist.github.com/Joshkunz/6946483
  [vlcwrap]: https://gist.github.com/Joshkunz/6410613
  [qmv]: https://gist.github.com/Joshkunz/a6791ecef6ac0d717921
