"""
This is the easy computer class, which extends the player class
"""
import random
from Player import P_Player
class EasyComputerPlayer(P_Player):
    
    def __init__(self, name):
        """initializes easy computer class"""
        super(EasyComputerPlayer,self).__init__(name)
    
    def roll_again(self,cage):
        """Randomly decides if the EasyCPU player will keep rolling."""

        ##MORE RISKY ROLL
        while cage.value < (10 + random.randint(2,20)):
            print( "Role again")
            return True
        print ("CPU will hold")
        return False