
# PigGame
![Pig face](https://raw.githubusercontent.com/heathermortensen/PigGame/master/pigFace.png)

* Pig is a dice rolling game, also known as Skunk.
* It has 2 screens.
* Screen #1 allows the user to enter the number of players in the game and their corresponding names.
* Screen #2 allows players to play Skunk and shows a scorecard.

### Java version of the dice rolling game = Skunk 
* I first programmed the Skunk game in Java using Eclipse. 
* It produced output to terminal.
* It is located in the [SkunkGame repo](https://github.com/heathermortensen/SkunkGame) of my Github page.
* A detailed description of game implemetation can be found in the SkunkGame README.md file.

### Python version of the dice rolling game = Pig.
* Pig frontend screens (screen1.py and screen2.py) were programmed in PyCharm using Tkinter on Windows.
* The backend will be translated from Java into Python using Spyder IDE shipped with Anaconda on Mac OSX.

#### Software installs

| Software     | Version   | Location
| ------------- | ---------- | ---------------------------- |
| Homebrew  | 2.4.0       | User/local/Cellular          | 
| Powershell  | 7.0.3       |                                         |
| OpenSSL    | 2.8.3       |                                         |
| pip              |                 |                                        |
| ------------- | ----------- | ----------------------------| 
| Anaconda   | 3              |                                        |
| Python        | 3.8           |                                        |
| Spyder        | 4.1.4        |                                        |
| Kite             |                 |                                        |
| ------------- | ----------- | ----------------------------|

### Step 1.) Design frontend

* I first designed both screens in Tkinter (UI framework inherent to python 3) to sketch out a basic layout for the game (see figures 1 and 2).
* These screens are running on Windows and Mac OSX, using python v3.8, and PIL/PILLO (which?).

#### File: screen1.py

![Screen #1 on Windows & Mac](https://raw.githubusercontent.com/heathermortensen/PigGame/master/screen1BothOS.png)

Figure 1. Screen 1 shows basic UI functionality when a button is clicked 


#### File: screen2.py

![Screen #2](https://raw.githubusercontent.com/heathermortensen/PigGame/master/screen2.png)

Figure 2. Screen 2 is where players will take turns rolling dice and a scorecard will be displayed

### Step 2.) Program frontend functionality

* Next, I started fresh. I programmed UI functionality into a blank file containing only necessary widgets that I required to test UI functionality.
* Design elements from screen1.py and screen2.py can be added in quickly later.
* This file is called piggy.py and contains a class for instantiating Window objects. 
* The window1 object contains the functionality for screen 1 (see figure 3).
* A second instantiaion of the Window object can be easily adopted to accomidate screen2.

#### File: piggy.py and its corresponding console output

![Window class](https://raw.githubusercontent.com/heathermortensen/PigGame/master/codeScreenshot1.png)

Figure 3. The Window class

* My class based window accepts user input for the number of players and the names of each player. 

![Screen Accepting user input](https://raw.githubusercontent.com/heathermortensen/PigGame/master/piggyUI_userInput.png)
![console output](https://raw.githubusercontent.com/heathermortensen/PigGame/master/consoleOutput.png)

Figure 5. UI functionality that accepts user input prior to begining a game of Pig

### Resources for merging this code together into Multiple class based windows and the backend:
* [Python: Tkinter Class Based Windows](youtube.com/watch?v=RkaekNkIKNY) - tutorial series on Udemy $15
* [Tkinter - GUI Example Multiple Display Frames](youtube.com/watch?v=KdoOm3xo8X0)


