#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:22:43 2020

@author: hm
"""

import tkinter as tk   #lowercase in python 3
# This is a seperate file inside the tkinter folder (lib/tkinter/ttk.py)
from tkinter import ttk
from PIL import Image, ImageTk

class PlayPig(tk.Tk):
    
    # arg = arguments, kwagrs = key word arguments = dictionaries
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # initialized tkinter
        container = tk.Frame(self) # init a Windows
        
        container.grid_rowconfigure(0, weight=1) # weight = 1 gives columns and rows equal priority
        container.grid_columnconfigure(0, weight=1) # weight = 1 gives columns and rows equal priority
        
        # Dictionary that holds all the different windows?
        self.frames = {}
        frame = StartPage(container, self) #StartPage = first page that we run
        
        #List of all the windows inside the application
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0)
        
        self.show_frame(StartPage)
        
        # End of initialization
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]   # cont is the key to grag a specific frame inside the dictionary line #24
        frame.tkraise() #Raises our selected frame/window to the top of the lsit
        
# Build a StartPage
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Pass in tkinter code so we see something on the window....
        # ///////////////////////////////////////////////
        
        root = tk.Tk(className='StartPage')
        root.iconbitmap('pig.ico')
        # set window size
        root.geometry("969x690")


        # RosyBrown colored box at top
        top_frame = tk.Frame(root, borderwidth=5)
        top_frame = tk.Frame(root, width=300, height=370, background="RosyBrown1")
        top_frame.grid(row=0, column=0, rowspan=3, columnspan=2, padx=(20, 20))
        # Give the frame a border, but it makes its label widgets disapear!
        # top_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)

        #set window color
        root.configure(bg='LightPink3')
        
        # myLabel00 = tk.Label(root, text=' \t \t  \t  \t  ', bg="RosyBrown1")
        # myLabel00.grid(row=0, column=0, columnspan=2)
        
        # Change the label to being attatched to the top_frame, not the root widget
        # myLabel0 = tkinter.Label(root, text='  I am fond of pigs. ')
        myLabel0 = tk.Label(top_frame, text='\n \n  I am fond of pigs.  \n', bg="RosyBrown1")
        myLabel0.config(font=("Courier", 10))
        myLabel0.grid(row=1, column=0)
        
        myLabel5 = tk.Label(top_frame, text='  Dogs look up to us.  \n', bg="RosyBrown1")
        myLabel5.config(font=("Courier", 10))
        myLabel5.grid(row=2, column=0)

        myLabel5 = tk.Label(top_frame, text='  Cats look down on us.  \n ', bg="RosyBrown1")
        myLabel5.config(font=("Courier", 10))
        myLabel5.grid(row=4, column=0)
        
        myLabel5 = tk.Label(top_frame, text='  Pigs treat us as equals.  \n', bg="RosyBrown1")
        myLabel5.config(font=("Courier", 10))
        myLabel5.grid(row=5, column=0)
        
        myLabel5 = tk.Label(top_frame, text='    ― Winston S. Churchill  \n \n \n \n ', bg="RosyBrown1")
        myLabel5.config(font=("Courier", 10))
        myLabel5.grid(row=6, column=0)
        
        myLabel1 = tk.Label(root, text='  Please enter number of players: ', background="mistyRose")
        myLabel1.config(font='Courier 14 bold')
        myLabel1.grid(row=2, column=0, rowspan=2, columnspan=2)

        e = tk.Entry(root, width=5, borderwidth=5)
        e.grid(row=2, column=3, rowspan=2)
        
        
        def myClick():
            myLabel3 = tk.Label(root, text=' does nothing', background="pink")
            myLabel3.grid(row=6, column=3)
        
        def myGameInstructionsButton():
            myLabel20 = tk.Label(root, text=' Yo ', background='Red')
            myLabel20.grid(row=4, column=3)
        
        def goToPageToRollDice():
            myLabel21 = tk.Label(root, text=' Yo ', background='Yellow')
            myLabel21.grid(row=5, column=3)
            
# This button should show this frame when clicked: bottom_frame
# https://www.delftstack.com/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/


        # This button was previously a tkinter.Button, but ttk.Button offers highlighting during mouse hover.
        myButton = tk.Button(root, text="Next", width=10, command=myClick)
        myButton.grid(row=3, column=3)
        
        myQuitButton = tk.Button(root, text="Show game rules", command=myGameInstructionsButton)
        myQuitButton.grid(row=7, column=0)
        
        myQuitButton = tk.Button(root, text="Quit game", command=root.quit)
        myQuitButton.grid(row=7, column=1)
        
        # myPlayGameButton = tk.Button(root, text="Play Pig", command=root.goToPageToRollDice())
        # myPlayGameButton.grid(row=7, column=2)
        
        # img = tk.PhotoImage("manRidesPig.png")

        try:
            img = ImageTk.PhotoImage(Image.open("manRidesPig.png"))
            myLabel4 = tk.Label(image=img)
            myLabel4.grid(row=1, column=4, columnspan=3, rowspan=10, padx=(20, 20))
        except IOError:
            print('image failed to load')
            pass
        
        assert isinstance(img, ImageTk.PhotoImage)
        
        # Pink box at bottom of screen displays rules
        bottom_frame = tk.Frame(root, borderwidth=5)
        bottom_frame = tk.Frame(root, width=300, height=300, background="Pink")
        bottom_frame.grid(row=6, column=0, rowspan=1, columnspan=1, padx=(20, 20))
        # Give the frame a black border
        bottom_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        
        # Game Instructions
        myLabel2 = tk.Label(bottom_frame, text='  Game Rules: ', background="pink")
        myLabel2.grid(row=4, column=0)
        myLabel2.config(font='Courier 12 bold')
        
        myLabel6 = tk.Label(bottom_frame, text=' - Player with most points wins. ', background="pink")
        myLabel6.grid(row=5, column=0)
        myLabel6.config(font='Courier 10 bold')
        
        myLabel7 = tk.Label(bottom_frame, text=' - In a tie, the first player looses. ', background="pink")
        myLabel7.grid(row=6, column=0)
        myLabel7.config(font='Courier 10 bold')
        
        myLabel8 = tk.Label(bottom_frame, text=' - Roll a 1 = lose points that turn. ', background="pink")
        myLabel8.grid(row=7, column=0)
        myLabel8.config(font='Courier 10 bold')
        
        myLabel9 = tk.Label(bottom_frame, text=' - Roll two 1s = lose ALL game points. ', background="pink")
        myLabel9.grid(row=8, column=0)
        myLabel9.config(font='Courier 10 bold')
        
        # root.mainloop()
        
   # /////////////////// End of 1st Pink screen with man riding a pig //////////////////////////////////     
app = PlayPig()
app.mainloop()

        