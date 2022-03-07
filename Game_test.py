import unittest
import sys
sys.path.append("Gamefile")
import unittest.mock
from unittest.mock import patch, MagicMock
from Player import P_Player
from EasyCom import EasyComputerPlayer
from HardCom import HardcomputerPlayer
from HumanPlayer import Human
from Dice import *
from Cage import Box
from Game import Game
import random
import os
import io

class TestGameClass(unittest.TestCase):
    def setUp(self):
        """ The SetUp """
        self.test_Game = Game()
        self.test_Game.players.append(Human("Test1"))
        self.test_Game.players.append(Human("Test2"))
        self.test_Game.current_player = 0
        self.test_Game.number_of_players = 2

    def test_Choose_player(self):
        """ Testing if there are two players created"""
        test_Game = Game()
        test_Game.Choose_players(username="user1", difficulty="Easy")
        self.assertTrue(len(test_Game.players) == 2)
        test_Game.players.clear()

        test_Game.Choose_players(username="user2", difficulty="Hard")
        self.assertTrue(len(test_Game.players) == 2)
        test_Game.players.clear()

        test_Game.Choose_players(username="user3", difficulty="Rigged")
        self.assertTrue(len(test_Game.players) == 2)
        test_Game.players.clear()
        
    def test_who_first(self):
        """ Testing if the method who rolles first works """
        self.test_Game.who_first()
        self.assertTrue(self.test_Game.current_player == 0 or self.test_Game.current_player == 1)
    
    def test_next(self):
        """ Testing if the method who rolles next works """
        x = self.test_Game.current_player
        self.test_Game.next()
        self.assertNotEqual(x, self.test_Game.current_player)

    def test_previous(self):
        """ Testing if the method who rolled previously works """
        x = self.test_Game.current_player
        self.test_Game.previous()
        self.assertNotEqual(x, self.test_Game.current_player)

    def test_roll_again(self):
        """ Test for the roll_again method """
        x = False
        y = False
        while True:
            try:
                new_roll = self.test_Game.die.roll()
                self.test_Game.box.add_dice_value(new_roll)
                self.assertGreater(self.test_Game.box.value, 0)
                x = True
            except RolledOneException:
                self.test_Game.box.reset()
                self.assertEqual(self.test_Game.box.value, 0)
                y = True                
            if x == True and y == True:
                break
    
    def tearDown(self):
        """ TearDown """
        if self.test_Game.players[0].f.closed is not True:
            self.test_Game.players[0].f.close()
        if self.test_Game.players[1].f.closed is not True:
            self.test_Game.players[1].f.close()

        self.test_Game.players.clear()
    
    
if __name__=="__main__":
    unittest.main()
