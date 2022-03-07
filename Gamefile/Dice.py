"""
This class represents the dice
"""
import random
class RolledOneException(Exception):
    pass
class Dice: 
    def __init__(self):
        """Initializes Dice"""
        self.value = random.randint(1,6)

    def roll(self):
        """rolls the dice"""
        self.value = random.randint(1,6)
        if self.value == 1: 
            raise RolledOneException
    
        return self.value

    def __str__(self):
        """returns the value to be printed"""
        return "Rolled " + str(self.value)


