# tkdisp.py
# Displays a text message in a GUI window for n [milli]seconds
'''
usage: tkdisp.py [-h] [-g GEOMETRY] [-bg BKGRD] [-fg FRGRD] [-fn FONT] [-fs FSIZE] [-b]
                 [-i] [-f]
                 msg tim

positional arguments:
  msg                   the message to be displayed
  tim                   milliseconds to display message

options:
  -h, --help            show this help message and exit
  -g GEOMETRY, --geometry GEOMETRY
                        WxH+left+top | size and position of window
  -bg BKGRD, --bkgrd BKGRD
                        background color of message window
  -fg FRGRD, --frgrd FRGRD
                        foreground color of message text
  -fn FONT, --font FONT
                        font family name of text
  -fs FSIZE, --fsize FSIZE
                        font size of message text
  -b, --bold            bold font for message text
  -i, --italic          italic font for message text
  -f, --isFile          msg is a filepath to a text file
'''

from tkinter import *
from tkinter import font
import sys
import argparse

parser = argparse.ArgumentParser(description='Display Gui Message')
parser.add_argument("msg", help="the message to be displayed")
parser.add_argument("tim", help="milliseconds to display message", type=int)
parser.add_argument("-g", "--geometry", default="+800+400",
                    help="WxH+left+top | size and position of window")
parser.add_argument("-bg", "--bkgrd", default="darkred",
                    help="background color of message window")
parser.add_argument("-fg", "--frgrd", default="white",
                    help="foreground color of message text")
parser.add_argument("-fn", "--font", default="Helvetica",
                    help="font family name of text")
parser.add_argument("-fs", "--fsize", default=12, type=int,
                    help="font size of message text")
parser.add_argument("-b", "--bold", action="store_true",
                    help="bold font for message text")
parser.add_argument("-i", "--italic", action="store_true",
                    help="italic font for message text")
parser.add_argument("-f", "--isFile", action="store_true",
                    help="msg is a filepath to a text file")


args = parser.parse_args()

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()
        if args.geometry.lower() == 'center':
            root.eval('tk::PlaceWindow . center')
        else:
            root.geometry(args.geometry) # WxH+left+top
        if args.tim < 1000:  # must have entered 'seconds'
            t = args.tim * 1000
        else:
            t = args.tim
        root.after(t, self.endit)

    def create_widgets(self):
        if args.bold:
            w = 'bold'
        else:
            w = 'normal'
        if args.italic:
            s = 'italic'
        else:
            s = 'roman'

        myfont = font.Font(family=args.font,
                           size=args.fsize,
                           weight=w,
                           slant=s)
        self.lbl = Label(self, text="",
                         bg=args.bkgrd,
                         font=myfont,
                         fg=args.frgrd,
                         height=3,
                         padx=8)

        self.lbl.pack(fill=BOTH, expand=True)

        if args.isFile:
            with open(args.msg, 'r') as file:
                msgText = file.read()
                self.lbl.configure(justify='left')
        else:
            msgText = args.msg

        self.lbl.configure(text=msgText)
        root.bind("<Button-1>", sys.exit)

    def endit(self):
        sys.exit()

#
root = Tk()
root.overrideredirect(True) # removed window decorations
root.attributes("-topmost", True)  # Keep on top of other windows
app = Application(master=root)
app.mainloop()
