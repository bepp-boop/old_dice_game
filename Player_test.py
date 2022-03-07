import unittest
import sys
sys.path.append("Gamefile")
from Player import P_Player
"""
This is a test class for Player
"""
class testPlayerClass(unittest.TestCase):
    def setUp(self):
        self.new_player = P_Player("Qyang")

    def test_init_default_object(self):
        """ The method tests if the player is initiliaze"""
        self.assertIsInstance(self.new_player,P_Player)

    def test_player_score(self):
        """The method test if the player score is working"""
        self.assertEqual(self.new_player.score,0)

    def test_player_name(self):
        """The method test if the player name is working"""
        self.assertEqual(self.new_player.name,"Qyang")

    def test_plus_score(self):
        """The method test if the plus score function is working"""
        self.new_player.plus_score(10)
        self.assertEqual(self.new_player.score,10)

    def test_set_name(self):
        """The method test if the set name function is working """
        self.new_player.set_name("Quang")
        self.assertEqual(self.new_player.name,"Quang")

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()

    