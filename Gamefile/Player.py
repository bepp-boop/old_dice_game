"""
This class represents players in general. HumanPlayer, HardCom andEasyCom extends this class
"""
class P_Player(object):
    def __init__(self, name = None):
        """initializes the player"""
        self.name = name
        self.score = 0
    
    def plus_score(self,player_score):
        """adds to the player's score"""
        self.score += player_score

    def set_name(self,name):
        """sets the name for the player"""
        self.name = name

    def __str__(self):
        """returns the player and their score"""
        return str(self.name) + ": " + str(self.score)