
# PigGame
![Pig face](https://raw.githubusercontent.com/heathermortensen/PigGame/master/pigFace.png)

* Pig is a dice rolling game (also known as Skunk).
* Screen #1 allows the user to enter the number of players in the game and their corresponding names.
* Screen #2 allows players to play Pig and displays a scorecard.

### Java version of the dice rolling game = Skunk 
* I first programmed the Skunk game in Java using Eclipse. 
* It produced output to terminal.
* It is located in the [SkunkGame repo](https://github.com/heathermortensen/SkunkGame) of my Github page.
* A detailed game description can be found in the SkunkGame [README.md](https://github.com/heathermortensen/SkunkGame/blob/master/README.md) file.

### Python version of the dice rolling game = Pig.
* Frontend screen designs (screen1.py and screen2.py) were sketchd out in PyCharm using python's Tkinter GUI frameowrk on Windows.
* The backend will be translated from Java into Python using Spyder IDE shipped with Anaconda on Mac OSX.

#### Software installs

| Software     | Version   | Location
| ------------- | ---------- | ---------------------------- |
| Homebrew  | 2.4.0       | Mac: User/local/Cellular | 
| Powershell  | 7.0.3       |                                         |
| OpenSSL    | 2.8.3       |                                         |
| pip              |                 |                                        |
| ------------- | ----------- | ----------------------------| 
| Anaconda   | 3              |                                        |
| Python        | 3.8           |                                        |
| Spyder        | 4.1.4        |                                        |
| Kite             |                 |                                        |
| ------------- | ----------- | ----------------------------|

### Step 1.) Frontend sketch

* I first designed both screens in Tkinter (UI framework inherent to python 3) to sketch out a basic layout for the game (see figures 1 and 2).
* I use the PIL Imaging Libary, which excludes me from using Pillow. (verify this - which did I install? They are mutually exclusive.)

#### File: screen1.py

![Screen #1 on Windows & Mac](https://raw.githubusercontent.com/heathermortensen/PigGame/master/screen1BothOS.png)

Figure 1. Screen 1 demonstrates basic button click to display game rules


#### File: screen2.py

![Screen #2](https://raw.githubusercontent.com/heathermortensen/PigGame/master/screen2.png)

Figure 2. Screen 2 is where players take turns rolling dice and a scorecard will be displayed

### Step 2.) Program frontend functionality

* Having aquainted with Tkinter, I started fresh. 
* I programmed into a blank file containing only necessary widgets required to test UI functions.
* Design elements from screen1.py and screen2.py can be added in quickly later.
* This file is called piggy.py and contains a class for instantiating Window objects. 
* The window1 object contains the functionality for screen 1 (see figure 3).
* A second instantiaion of the Window object can be easily adopted to accomidate screen2.

#### File: piggy.py and its corresponding console output

![Window class](https://raw.githubusercontent.com/heathermortensen/PigGame/master/codeScreenshot1.png)

Figure 3. The Window class

* The class based window accepts and validates user input for the number of players and the names of each player. 

![userInputValidation](https://raw.githubusercontent.com/heathermortensen/PigGame/master/userInputScreenshot.png)

Figure 4. User input validation for screen 1

* This step concludes basic programming for the View in MVC.

![console output](https://raw.githubusercontent.com/heathermortensen/PigGame/master/consoleOutputPiggy.png)

Figure 5. User input required to run the program

### Step 3.) Program the backend
- Remember to make the controller navigate to the 2nd window (not the 1st window)

* write something here...

### Resources for merging this frontend (multiple class based windows) together with the python backend:
* [Python: Tkinter Class Based Windows](youtube.com/watch?v=RkaekNkIKNY) - tutorial series on Udemy $15
* [Tkinter - GUI Example Multiple Display Frames](youtube.com/watch?v=KdoOm3xo8X0)
* [Model View Controller Pattern](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm)
* [Object Oriented Programming Crash Course with Tkinter](https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/)
* [An Example of Model View Controller Design Pattern with Tkinter Python](https://sukhbinder.wordpress.com/2014/12/25/an-example-of-model-view-controller-design-pattern-with-tkinter-python/)
* [tkinter — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
* Python QT framework for the next time I do something like this:
* [Qt for Python](https://doc.qt.io/qtforpython/)
* How to make an executable:
* [Standalone Python EXE Executable - Python Tkinter GUI Tutorial #40](https://www.youtube.com/watch?v=QWqxRchawZY)
* [How to Convert any Python File to .EXE](https://www.youtube.com/watch?v=UZX5kH72Yx4)
