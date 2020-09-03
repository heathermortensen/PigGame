from tkinter import *
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
    # int player_names[] = new player_names[number_of_players]

    def __init__(self, root, title, geometry, message, iconbitmap,
                 playerNumber):

        self.root = root  # this is the instance variable for the entire window
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.iconbitmap(iconbitmap)
        self.number_of_players = playerNumber
        # Make the window show up in center of screen and not be ccovered up by anything else.
        # self.root.eval('tk::PlaceWindow %s center' % self.root.wininfo_toplevel())
        # this is an important line.
        # self.root.mainloop()

        def addPlayers():
            """Allows user to input the number of and names of all game players"""
            # stackoverflow.com/questions/12169258/should-i-use-entrys-get-or-its-textvariables-for-tkinter-in-python

            print("\nInitial # of players (Line #26) = " + str(self.number_of_players))

            # Collects user input from the entry and turns it into an int
            # user_input_number_of_players.set(int(str(entry_player_number.get("1.0", 'end-1c'))))
            try:
                user_input_number_of_players = int(entry_player_number.get())
                print("Inside try block, user_input = " + str(user_input_number_of_players))
                self.number_of_players = user_input_number_of_players

            except ValueError:
                tkinter.messagebox.showerror('Non-Integer Input', 'User MUST enter a player # greater than 1.', icon = 'error')
                # tkinter.messagebox.deiconify()
                # tkinter.messagebox.quit()
                # tkinter.messagebox.destroy()
            
            #user_input_number_of_players.set(int(str(entry_player_number.get("1.0", 'end-1c'))))
            

           # Add a label

            myLabel1b = tkinter.Label(self.root, text="Please Enter Player Names: ",
                                 width=25)
            myLabel1b.config(font="Courier 14 bold")
            myLabel1b.grid(row=2, column=1)
            
            #Make a scrollable frame appear
            
            # You must create a frame, embed that in the canvas, then attach the scrollbar to the canvas
            # Code for scrollable frame came from:
            # https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
            myframe=Frame(root,relief=GROOVE,width=100,height=100)
            myframe.grid(row=3,column=3, columnspan=2)

            canvas=Canvas(myframe)
            frame=Frame(canvas)
            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)
            
            # myframe.bind(
            #    "<Configure>",
            #    lambda e: canvas.configure(
            #        scrollregion=canvas.bbox("all")
            #        )
            #    )
            
            # put entry boxes for player names inside the scrollable frame
            
            for x in range(self.number_of_players):
                print(x+1)
                # Add a label
                myLabel1b = tkinter.Label(myframe, text="Player #" + str(x+1)+ " Name: ")
                myLabel1b.config(font="Courier 14 bold")
                myLabel1b.grid(row=4+x, column=3)
                
                # Fix this textVariable parameter - unecessary?
                # https://stackoverflow.com/questions/32640219/creating-stringvar-variables-in-a-loop-for-tkinter-entry-widgets
                
                # user_input_player_names = tkinter.StringVar()
                name_entries = []
                for i in range(self.number_of_players):
                    entry_player_name = tkinter.Entry(myframe, width=10, borderwidth=2)
                    # entry_player_name.set(str(x+1))
                    entry_player_name.grid(row=4+x, column=4)
                    name_entries.append(entry_player_name)
                # specify a default value inside the entry box
                # entry_player_number.insert(0,int("2"))

            # Add a button for adding players names into the game

            addPlayerNamesButton = tkinter.ttk.Button(self.root,
                                     text="Enter Names",
                                     command=addPlayerNames)

            addPlayerNamesButton.grid(row=x+2, column=4)
                
            # Make old label, entry, and button dissapear
            
            myLabel1.grid_forget()
            entry_player_number.grid_forget()
            addPlayerButton.grid_forget()
           
                
                #myLabel1.congifg(text="Please Enter Player Names: ", width=25)
                # myLabel1.config(font="Courier 14 bold")
                # myLabel1.grid(row=2, column=1)
          
        

            print("# of players after button click = " + str(self.number_of_players))
            # Set class instance value to this input from the user
            return self.number_of_players
        
        print("# of players after click = " + str(self.number_of_players))
        
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

        self.root.mainloop()

        pass

    pass


main()
