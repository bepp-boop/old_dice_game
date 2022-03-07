import unittest
import sys
sys.path.append("Gamefile")

from Dice import Dice
from Dice import RolledOneException
from contextlib import suppress

""" This is a test that tests the class called dice
 There are three test methods  
"""

class TestDiceClass(unittest.TestCase):
    def setUp(self):
        """Setup dice object"""
        self.new_Dice = Dice()

    def test_init_default_object(self):
        """ Tests if an dice is an instance"""
        self.assertIsInstance(self.new_Dice, Dice)

    def test_roll(self):
        """ Rolling the dice """
        try:
            roll = self.new_Dice.roll()
        except RolledOneException:
            roll = 1
        ifroll = (1 <= roll <= 6)
        """ Checking if the roll is within a range from 1 to 6 """
        self.assertTrue(ifroll)

    
    def test_random(self):
        """ Creates a list """
        numbers = []
        i = 0
        try:
            """ Rolling the dice and appending it to the create list """
            numbers.append(self.new_Dice.roll())
        except RolledOneException:
            numbers.append(1)

        while i < 10:
            i = i + 1
            try:
                numbers.append(self.new_Dice.roll())
            except RolledOneException:
                numbers.append(1)
            if numbers[i] != numbers[i-1]:
                break
                
        """ Checking if lists are not equal """
        self.assertNotEqual(numbers[i],numbers[i-1])

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
