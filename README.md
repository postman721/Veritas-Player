# Veritas-Player
Veritas Player is a Python  media player that uses Videolans Vlc as a backend.

![veritas](https://user-images.githubusercontent.com/29865797/28453374-c43e043e-6dff-11e7-92ab-0f7f3a5472c9.jpg)

Veritas is written with Python and Gtk3 and it uses Videolan´s Python module to achieve things in its backend. In other words: it has features of Vlc in it.

The v.1 release of Veritas Player has the following functionality:

– It can play songs.

– It can open video files and play them.

– It has all the regular playback functionalities:Play, pause, rewind, go forward etc.

-It can open dvds and play them. Note. If your dvd is encrypted then you might need to install libdvdcss2 or similar from some online sources. Libdvdcss2 is not included in Veritas Player by default – and never will be.

– Support for some common shortkeys. See more from the about dialog of Veritas.

– Vertias has a slider, which calculates the progress of a song or media file. If the slider is moved then the position is changed.

-Veritas prints the name of the file that is currently playing and also the number of elements in the playlist.

Tip. Veritas does not currently move automatically to the next object on the playlist. You can easily navigate between previous/next objects by writing the object number to the line and pressing enter. See the screenshot above.

Licenses

#Veritas Player Copyright (c) 2017 JJ Posti <techtimejourney.net>

#The program comes with ABSOLUTELY NO WARRANTY;

#for details see: http://www.gnu.org/copyleft/gpl.html.

#This is free software, and you are welcome to redistribute it under

#GPL Version 2, June 1991″)

#Note vlc.py is from Videolan and it is not covered by the GPL license.

#Vlc.py is under LGPL 2.1 and remains an unmodified and imported module in Veritas Player.

Dependencies:

Python: python3-gi and python3 should be enough in most cases. You might need to install something more depending on your distribution of choice. Also, the Vlc Python module is required. By default you should keep the Vlc module and Veritas Player in the same folder.

Important additions: Since this is Vlc based it needs vlc as a backend. So, install vlc-nox package or similar. If you want to play Dvds that have menus in them, you also have to install libdvdnav4 or similar. In most cases, both, libdvdnav4 and libdvdcss2 are needed. For Libdvdcss2 Google: Debian Multimedia (a website).


Running Veritas


If needed, make files executable with chmod +x some_file.py

Run with command: python some_location/veritas.py

Tip. If you have songs on a cd and you want to get them to your computer, consider installing, for example, sound-juicer.
If you want lightweight, you might want to consider ripperx instead of sound-juicer.

____________________________________
Original post is at:
http://www.techtimejourney.net/veritas-player-arrives/
