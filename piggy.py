# from tkinter import *
import tkinter
from PIL import Image, ImageTk
# The next 2 imports override the basic Tk widgets
# widget options that use fg and bg will no longer work. 
# Must use, instead, ttk.Style class
from tkinter import ttk
from tkinter.ttk import *
# See docs.python.org/8/library/tkinter.ttk.html

# Class Based Windows
# youtube.com/watch?v=RkaekNkIKNY

# Tkinter - GUI Eaxample Multiple Display Frames
# youtube.com/watch?v=KdoOm3xo8X0


def main():
    root = tkinter.Tk()
    window1 = Window(root, "Play_a_game_of_Pig", "969x690", "someMessage",
                     "pig.ico", 0)

    return None


class Window:
    number_of_players = 0

    def __init__(self, root, title, geometry, message, iconbitmap,
                 playerNumber):

        self.root = root  # this is the instance variable for the entire window
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.iconbitmap(iconbitmap)
        self.number_of_players = playerNumber

        def addPlayers(self):
            """Allows user to input the number of and names of all game players"""
            # stackoverflow.com/questions/12169258/should-i-use-entrys-get-or-its-textvariables-for-tkinter-in-python

            print("/n initial # of players = " + str(self.number_of_players))

            # Collects user input from the entry and turns it into an int
            user_input_number_of_players.set(int(str(entry_player_number.get("1.0", 'end-1c'))))

            # Set class instance value to this input from the user
            self.number_of_players = user_input_number_of_players

            print("# of players after click = " + str(self.number_of_players))

        return None

        # Add a label

        myLabel1 = tkinter.Label(self.root, text="Please Enter # of Players",
                                 width=25)
        myLabel1.config(font="Courier 14 bold")
        myLabel1.grid(row=2, column=1)

        # bind user input to a variable from the entry box.
        # Specifies a name whose value is linked to the widget value.

        user_input_number_of_players = tkinter.StringVar()

        # add an entry box

        entry_player_number = tkinter.Entry(self.root, width=5, borderwidth=5,
                                            textvariable=user_input_number_of_players)
        # number.set(int("0"))
        entry_player_number.grid(row=2, column=3, rowspan=2)
        # specify a default value inside the entry box
        # entry_player_number.insert(0,int("2"))

        # Add a button for adding players to the game

        addPlayerButton = tkinter.ttk.Button(self.root,
                                     text="Enter",
                                     command=addPlayers)

        addPlayerButton.grid(row=2, column=4)

        # this is an important line.
        self.root.mainloop()

        pass

    pass


main()

   