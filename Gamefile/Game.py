"""
This class represents the game, and does most of the heavy lifting
"""
from Player import P_Player
from EasyCom import EasyComputerPlayer
from HardCom import HardcomputerPlayer
from HumanPlayer import Human
from Dice import *
from Cage import Box
import random
import os

class Game:
    def __init__(self):
        """initializes game"""
        self.players = []
        self.die = Dice()
        self.box = Box()

    def Choose_players(self, username=None, difficulty=None):
        """Function when you start the game. It's begin with the current players."""
        if username is None:
            username = str(input("Enter your username "))
        self.players.append(Human(username))
        is_test = difficulty is not None
        while True:
            if difficulty is None:
                difficulty = str(input("Pick your difficulty: Easy, Hard, Rigged, or Player? "))

            if difficulty == "Easy":
                self.players.append(EasyComputerPlayer("Simply MrRobot"))
                break
            elif difficulty == "Hard" :
                self.players.append(HardcomputerPlayer("Hard MrRobot"))
                break
            elif difficulty == "Rigged" :
                self.players.append(HardcomputerPlayer("Rigged MrRobot"))
                self.players[1].plus_score(random.randint(25, 75))
                break
            elif difficulty == "Player" :
                username2 = str(input("Enter your username "))
                self.players.append(Human(username2))
                break
            print("Not a valid option, choose again!")
            if is_test is True:
                break
            difficulty = None



    def who_first(self):
        """decides what player goes first"""
        self.number_of_players = len(self.players)
        self.current_player = random.randint(1,2) % self.number_of_players
        print('{} starts'.format(self.players[self.current_player].name))
        
    def next(self):
        """moves to the next player"""
        self.current_player = (self.current_player + 1) % self.number_of_players
        
    def previous(self):
        """moves to the previous player"""
        self.current_player = (self.current_player - 1) % self.number_of_players

    def scores(self):
        """returns player scores"""
        return' , '.join(str(x)for x in self.players)

    def play(self):
        """plays the game"""
        self.who_first()    
        while all(player.score < 100 for player in self.players):
            print('\nCurrent score --> {}'.format(self.scores()))
            print('\n*** {} to play ***'.format(self.players[self.current_player].name))
            self.box.reset()
            
            while self.roll_again():
                pass    

            self.players[self.current_player].plus_score(self.box.value)
            self.next()
        self.previous()
        self.players[0].f.write("{} \n".format(str(self.players[0].score)))
        self.players[0].f.close()
        if self.players[1].name != "Simply MrRobot" and self.players[1].name != "Hard MrRobot" and self.players[1].name != "Rigged MrRobot":
            self.players[1].f.write("{} \n".format(str(self.players[1].score)))
            self.players[1].f.close()
        print(' {} has won '.format(self.players[self.current_player].name))

    def roll_again(self):
        """Adds rolled dice to box. Returns if human/cpu wants to continue.

        If either player rolls a 1, the box value is reset, and turn ends.
        """
        try: 
            dice_value = self.die.roll()
            self.box.add_dice_value(dice_value)
            print('Last roll: {}, new box value: {}'.format(dice_value, self.box.value))
            return self.players[self.current_player].roll_again(self.box)
            
        except RolledOneException:
            print(' Rolled one. Switch turn.')
            self.box.reset()
            return False
