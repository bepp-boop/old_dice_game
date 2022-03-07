"""
This class represents the hard computer player, which extends the player class
"""
import random
from Player import P_Player
class HardcomputerPlayer(P_Player):

    def __init__(self, name):
        """initializes hard computer player"""
        super(HardcomputerPlayer,self).__init__(name)
    
    def roll_again(self,cage):
        """Randomly decides if the hard computer player will keep rolling."""

        while cage.value < (6 + random.randint(20,40)):
            print( "Roll again")
            return True
        print ("CPU will hold")
        return False