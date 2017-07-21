#!/usr/bin/env python
#Veritas Player Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#Note vlc.py is from Videolan and it is not covered by the GPL license. 
#Vlc.py is under LGPL 2.1 and remains an unmodified imported module in Veritas Player.

#IMPORTING MODULES
import sys, os, time, gi, vlc
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, Gio
gi.require_version('GdkX11', '3.0')
from gi.repository import GdkX11, GLib
from vlc import Media, MediaPlayer
class Veritas(Gtk.Window):

    def esc_event(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "F11":
            if self.full:
                self.player.set_fullscreen(False)
                self.full=False
                self.window1.unfullscreen()
                self.toolbar.show()
                self.slider.show()
                self.line.show()
                self.label.show()       
            else:
                self.player.set_fullscreen(True)
                self.full= True
                self.window1.fullscreen()
                self.toolbar.hide()
                self.slider.hide()
                self.line.hide()
                self.label.hide()
                         
    def file_event(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "F10":
            self.selected(widget)          
        else:
            pass

    def pause_event(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "p":
            self.play(widget)          
        else:
            pass
      
    def about1 (self, widget):
        about1 = Gtk.AboutDialog()
        about1.set_program_name("Veritas Player")
        about1.set_version("V.1")
        about1.set_copyright(" Copyright (c) 2017 JJ Posti <techtimejourney.net>")
        about1.set_comments("Veritas Player is a player application written with Python and Gtk3.The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. The GUI is free software, and you are welcome to redistribute it under GPL Version 2, June 1991. ______________________________________________________________________________ Note vlc.py is from Videolan and it is not covered by the GPL license. Vlc.py is under LGPL 2.1 or (at your option) any later version. Vlc.py remains as an unmodofied imported module in Veritas Player. ___________________________________________________________________________ Shortkeys: p: Pause/resume playback, F11: Toggle Fullscreen, F10: Add files.")
        about1.set_website("www.techtimejourney.net")
        about1.run() 
        about1.destroy()

    def selected(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose files", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        dialog.set_select_multiple(True)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.open_me=(dialog.get_filenames())
            for item in self.open_me:
                self.numbers=len(self.open_me)
                starting=self.open_me[0]
                print starting
                self.player.set_mrl(str(starting))
                self.name=os.path.basename(str(self.open_me))
                self.label.set_text(self.name)        
                self.play(widget)

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")
        dialog.destroy()
        return self.open_me, self.numbers

    def selected_folder(self,widget):
        self.line.show()
        run="dvd://"
        print run
        self.open_me=str(run)
        self.player.set_mrl(run)
        self.player.play()
       
    def sized(self,widget):
        self.inits=self.player.get_length()
        seconds=(self.inits/1000)%60
        minutes=(self.inits/(1000*60))%60
        hours=(self.inits/(1000*60*60))%24
        self.everything=('Hours:', hours, 'Minutes:', minutes, 'Seconds:', seconds)
        print self.everything
    
    def clip_about(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, os.path.basename(str(self.open_me)))
        dialog.run()
        print("INFO dialog closed")
        dialog.destroy()

#Postion
    def position(self, widget):
        val = self.slider.get_value()
        ax=self.player.get_length()
        pros= ax/100
        if val == 0:
            self.player.set_time(ax - ax)
        
        elif val == 1:
            self.player.set_time(1 * pros)
            
        
        elif val == 2:
            self.player.set_time(2 * pros)
       
        elif val == 3:
            self.player.set_time(3 * pros)
        
        elif val == 4:
            self.player.set_time(4 * pros)
       
        elif val == 5:
            self.player.set_time(5 * pros)
        
        elif val == 6:
            self.player.set_time(6 * pros)
 
        elif val == 7:
            self.player.set_time(7 * pros)

        elif val == 8:
            self.player.set_time(8 * pros)

        elif val == 9:
            self.player.set_time(9 * pros)

        elif val == 10:
            self.player.set_time(10 * pros)
###################################################################
        elif val == 11:
            self.player.set_time(11 * pros)
        elif val == 12:
            self.player.set_time(12 * pros)
       
        elif val == 13:
            self.player.set_time(13 * pros)
        
        elif val == 14:
            self.player.set_time(14 * pros)
       
        elif val == 15:
            self.player.set_time(15 * pros)
        
        elif val == 16:
            self.player.set_time(16 * pros)
 
        elif val == 17:
            self.player.set_time(17 * pros)

        elif val == 18:
            self.player.set_time(18 * pros)

        elif val == 19:
            self.player.set_time(19 * pros)

        elif val == 20:
            self.player.set_time(20 * pros)

#####################################################################
        elif val == 21:
            self.player.set_time(21 * pros)
        elif val == 22:
            self.player.set_time(22 * pros)
       
        elif val == 23:
            self.player.set_time(23 * pros)
        
        elif val == 24:
            self.player.set_time(24 * pros)
       
        elif val == 25:
            self.player.set_time(25 * pros)
        
        elif val == 26:
            self.player.set_time(26 * pros)
 
        elif val == 27:
            self.player.set_time(27 * pros)

        elif val == 28:
            self.player.set_time(28 * pros)

        elif val == 29:
            self.player.set_time(29 * pros)


        elif val == 30:
            self.player.set_time(30 * pros)

####################################################################
        elif val == 31:
            self.player.set_time(31 * pros)
        elif val == 32:
            self.player.set_time(32 * pros)
       
        elif val == 33:
            self.player.set_time(33 * pros)
        
        elif val == 34:
            self.player.set_time(34 * pros)
       
        elif val == 35:
            self.player.set_time(35 * pros)
        
        elif val == 36:
            self.player.set_time(36 * pros)
 
        elif val == 37:
            self.player.set_time(37 * pros)

        elif val == 38:
            self.player.set_time(38 * pros)

        elif val == 39:
            self.player.set_time(39 * pros)

        elif val == 40:
            self.player.set_time(40 * pros)
###########################################################################
        elif val == 41:
            self.player.set_time(41 * pros)
        elif val == 42:
            self.player.set_time(42 * pros)
       
        elif val == 43:
            self.player.set_time(43 * pros)
        
        elif val == 44:
            self.player.set_time(44 * pros)
       
        elif val == 45:
            self.player.set_time(45 * pros)
        
        elif val == 46:
            self.player.set_time(46 * pros)
 
        elif val == 47:
            self.player.set_time(47 * pros)

        elif val == 48:
            self.player.set_time(48 * pros)

        elif val == 49:
            self.player.set_time(49 * pros)

        elif val == 50:
            self.player.set_time(50 * pros)

######################################################################
        elif val ==51:
            self.player.set_time(51 * pros)
        elif val == 52:
            self.player.set_time(52 * pros)
       
        elif val == 53:
            self.player.set_time(53 * pros)
        
        elif val == 54:
            self.player.set_time(54 * pros)
       
        elif val == 55:
            self.player.set_time(55 * pros)
        
        elif val == 56:
            self.player.set_time(56 * pros)
 
        elif val == 57:
            self.player.set_time(57 * pros)

        elif val == 58:
            self.player.set_time(58 * pros)

        elif val == 59:
            self.player.set_time(59 * pros)


        elif val == 60:
            self.player.set_time(60 * pros)
########################################################
        if val ==61:
            self.player.set_time(61 * pros)
        elif val == 62:
            self.player.set_time(62 * pros)
       
        elif val == 63:
            self.player.set_time(63 * pros)
        
        elif val == 64:
            self.player.set_time(64 * pros)
       
        elif val == 65:
            self.player.set_time(65 * pros)
        
        elif val == 66:
            self.player.set_time(66 * pros)
 
        elif val == 67:
            self.player.set_time(67 * pros)

        elif val == 68:
            self.player.set_time(68 * pros)

        elif val == 69:
            self.player.set_time(69 * pros)

        elif val == 70:
            self.player.set_time(70 * pros)
##########################################################
        elif val == 71:
            self.player.set_time(71 * pros)
        elif val == 72:
            self.player.set_time(72 * pros)
       
        elif val == 73:
            self.player.set_time(73 * pros)
        
        elif val == 74:
            self.player.set_time(74 * pros)
       
        elif val == 75:
            self.player.set_time(75 * pros)
        
        elif val == 76:
            self.player.set_time(76 * pros)
 
        elif val == 77:
            self.player.set_time(77 * pros)

        elif val == 78:
            self.player.set_time(78 * pros)

        elif val == 79:
            self.player.set_time(79 * pros)

        elif val == 80:
            self.player.set_time(80 * pros)

#######################################################################
        elif val == 81:
            self.player.set_time(81 * pros)
        elif val == 82:
            self.player.set_time(82 * pros)
       
        elif val == 83:
            self.player.set_time(83 * pros)
        
        elif val == 84:
            self.player.set_time(84 * pros)
       
        elif val == 85:
            self.player.set_time(85 * pros)
        
        elif val == 86:
            self.player.set_time(86 * pros)
 
        elif val == 87:
            self.player.set_time(87 * pros)

        elif val == 88:
            self.player.set_time(88 * pros)

        elif val == 89:
            self.player.set_time(89 * pros)

        elif val == 90:
            self.player.set_time(90 * pros)
###################################################################
        if val == 91:
            self.player.set_time(91 * pros)
        elif val == 92:
            self.player.set_time(92 * pros)
       
        elif val == 93:
            self.player.set_time(93 * pros)
        
        elif val == 94:
            self.player.set_time(94 * pros)
       
        elif val == 95:
            self.player.set_time(95 * pros)
        
        elif val == 96:
            self.player.set_time(96 * pros)
 
        elif val == 97:
            self.player.set_time(97 * pros)

        elif val == 98:
            self.player.set_time(98 * pros)

        elif val == 99:
            self.player.set_time(99 * pros)

        elif val == 100:
            self.player.set_time(100 * pros)
#Play
    def play(self,widget):
        self.name=os.path.basename(str(self.open_me))
        self.label.set_text(self.name)
        self.i=0
        starting=self.open_me[self.i]
        self.name=os.path.basename(str(starting))
        self.total=str(self.numbers)
        self.label.set_text(self.name + '  ' 'Number of songs:' + '  ' + self.total)
        self.player.play()
        
        if self.Paused:
            self.player.play()
            self.Paused=True
           
        else:
            self.player.pause()
            self.Paused = False
            return self.total
        	
#Forward 1 second
    def one_forward(self,widget):
        self.player.set_time(self.player.get_time() + 1000)

#Back 1 second
    def one_back(self,widget):
        self.player.set_time(self.player.get_time() - 1000)
    
#Stop
    def stop(self,widget):
        self.player.stop()
        
#Previous/Next
    def prev(self,widget):
        self.line.show()
        run=self.line.get_text()
        int_run=int(run)
        print run  
        if self.numbers > 0:
            print self.i
            starting=self.open_me[int_run]
            print starting
            self.player.set_mrl(str(starting))        
            self.play(widget)
            self.i= self.i - 1 
            self.label.set_text('')
            self.name=os.path.basename(str(starting))
            self.label.set_text(self.name + '  ' 'Number of songs:' + '  ' + self.total)
            print self.i
                
    def time_scale(self,widget):    
        self.in1=self.player.get_length()
        self.time2=self.player.get_time()
        calc1= (float(self.time2))
        calc2= (float(self.in1))
        calc_final= calc1/calc2
        calc_procent= calc_final * 100
        self.slider.set_value(calc_procent)
        return True
                
    def init_me(self, widget, data=None):
        self.vlcInstance = vlc.Instance("--no-xlib", "--fullscreen")
        self.player = self.vlcInstance.media_player_new()
        win_id = widget.get_window().get_xid()
        self.player.set_xwindow(win_id)
        self.is_player_active = True        
####################################
#STARTING WINDOW DEFINITIONS
#################################
#GENERAL STUFF
#################################    
    def __init__(self, *args, **kwargs):
        super(Veritas, self).__init__(*args, **kwargs)                   
# Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_decorated(True)
        self.window1.set_size_request(700,400)
        self.window1.set_keep_below(False)
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.stick()
        self.window1.set_title("Veritas Player")
        self.window1.connect("key-press-event", self.esc_event)
        self.window1.connect("key-press-event", self.file_event)
        self.window1.connect("key-press-event", self.pause_event)

#Media line
        self.line=Gtk.Entry()
        self.line.set_placeholder_text("Enter song number. First song starts from the number 0, second song is 1 etc.")
        self.line.connect("activate", self.prev)

#Label
        self.label=Gtk.Label()
        
#Slider
        self.slider= Gtk.HScale()
        self.slider.set_range(0, 100)
        self.slider.set_increments(1, 10)
        self.slider.set_digits(0)
        self.slider.set_size_request(160, 35)
        self.slider.connect("value-changed", self.position)

#Pause / Unpause/ Screen status placeholder variables
        self.Paused = False
        self.full= False
						
#Toolbar and others
        self.toolbar=Gtk.Toolbar()
        self.separator=Gtk.Separator()
        
#Tools and buttons               
        self.rew_button=Gtk.ToolButton(Gtk.STOCK_MEDIA_REWIND)
        self.rew_button.connect("clicked", self.one_back)
        self.rew_button.set_label("Rewind")
        self.rew_button.set_tooltip_text ("Rewind 1 second")                    
        self.toolbar.insert(self.rew_button, -1)
        
        self.for_button=Gtk.ToolButton(Gtk.STOCK_MEDIA_FORWARD)
        self.for_button.connect("clicked", self.one_forward)
        self.for_button.set_label("Forward")
        self.for_button.set_tooltip_text ("Forward 1 second")                    
        self.toolbar.insert(self.for_button, -1)
        
        self.stop_button=Gtk.ToolButton(Gtk.STOCK_MEDIA_STOP)
        self.stop_button.connect("clicked", self.stop)
        self.stop_button.set_label("Stop")
        self.stop_button.set_tooltip_text ("Stop")                    
        self.toolbar.insert(self.stop_button, -1)
                        
        self.dvd_button=Gtk.ToolButton(Gtk.STOCK_CDROM)
        self.dvd_button.set_label("Open DVD")
        self.dvd_button.set_tooltip_text ("Open DVD")                    
        self.dvd_button.connect("clicked", self.selected_folder)
        self.toolbar.insert(self.dvd_button, -1)
        
        self.clip_button=Gtk.ToolButton(Gtk.STOCK_INFO)
        self.clip_button.connect("clicked", self.about1)
        self.clip_button.set_label("About")
        self.clip_button.set_tooltip_text ("About")                    
        self.toolbar.insert(self.clip_button, -1)
        
#Next song placeholder
        self.i=0
        
#Drawing area for the canvas
        self.draw = Gtk.DrawingArea()
        self.draw.connect("realize",self.init_me)

#Containers
        self.vbox=Gtk.VBox()
        self.vbox.pack_start(self.toolbar, False, False, 0)
        self.vbox.pack_start(self.line, False, False, False)
        self.vbox.pack_start(self.draw, True, True, 0)
        self.vbox.pack_start(self.slider, False, False, False)
        self.vbox.pack_start(self.label, False, True, False)
    
#Horizontal containers
        self.hbox=Gtk.HBox()
        self.hbox.pack_start(self.vbox, True, True, True)
        
#Colors   
        self.hbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0.25))
        self.vbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0.25))
        self.toolbar.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0.25))
        self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0.25))

#Show everything
        self.window1.add(self.hbox)		
        self.window1.show_all()
         
#Making window resizable and enabling the hide window connector        
        self.window1.set_resizable(True)
        self.window1.connect("destroy", Gtk.main_quit)
   
def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    start=Veritas()
    GLib.timeout_add(2000, start.time_scale, None)
    main()
