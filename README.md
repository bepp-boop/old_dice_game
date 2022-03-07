# Pig_Game

This is a project in which is developed a program for a Pig Game. 

# Authors

Alrik Strömblad, Sara Momiroska, Quang Minh Nguyen

# About the Game

Pig game is a simple dice game that is typically played by several players. All players take turns to roll a single die as many times as they wish, as they roll the points are added resulting in a total value, however their gained score is lost for the turn if they roll a 1.
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold", when they decide to hold, the score remains until teir next turn. If the player rolls a 1, they score nothing and it becomes the next player's turn. The first player who gaines 100 or more points wins.

Example of a situation:
Two players Adam and Simon play pig game. Adam rolls four times and gets a 5-4-6-2 and on the fifth round he decides to hold. Now his score is 17. Simon rolls 6-3-1. After this round Simon has 0 points.

# About the program

The program is written in Python using object oriented programming style. The program consists of 8 classes which include Main, Player, Game, HumanPlayer, HardComp, EasyComp, Dice, Cage. All of the classes and the methods in them are tested through test-driven development method.The program makefile also run exculsively with window command prompt. 

# Download chocolatey
You should have choco install in your laptop before anything.You will need to follow the intrustion in this link. https://chocolatey.org/install

# Download make
After download chocolatey you can download make to used the command prompt in makefile. 
This can be done by typing "choco install make"

# update pip
In the virtual environment (myenv\Scripts\activate from a02 file in terminal)
on mac:
```bash
pip3 install pip --upgrade
```

on win:
```bash
pip install pip --upgrade
```

# Generate UML
To used the uml file in the pylint. You will need to to download the grahpiviz in your file. This can be done by typing "choco install graphviz"

# Install the nessary packages
You can then download the file in requirements.txt in your vertiual enviroment by using different command prompt in makefile. "make install"




