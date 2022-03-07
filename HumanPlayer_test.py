import unittest
import unittest.mock
from unittest.mock import patch, MagicMock
import sys
sys.path.append("Gamefile")

import os 
from HumanPlayer import Human

class TestHumantest(unittest.TestCase):

    def setUp(self):
        """Setting up human class"""
        self.new_player = Human("Test1")

    def test_init_default_object(self):
        """Test if human object is initilize"""
        self.assertIsInstance(self.new_player, Human)

    def test_Human_name(self):
        """Test if the name varible existed"""
        self.assertEqual(self.new_player.name,"Test1")

    def test_Human_score(self):
        """Test if the score function and varible worked"""
        self.new_player.plus_score(10)
        self.assertEqual(self.new_player.score,10)

    def test_Human_set_name(self):
        """Test if the set function work"""
        self.new_player.set_name("Not Test1")
        self.assertEqual(self.new_player.name,"Not Test1")

    @patch('builtins.input', side_effect = ['1', '10','5'])
    def test_cheat(self, mock_inputs):
        """tests the access menu's ability to cheat"""
        self.new_player.access_menu()
        self.assertEqual(self.new_player.score, 10)

    @patch('builtins.input', side_effect = ['2', 'Alrik', 'Test3', '5'])
    def test_rename(self, mock_inputs):
        """tests the access menu's ability to rename the player"""
        self.new_player.access_menu()
        self.assertEqual(self.new_player.name, 'Test3')

    @patch('builtins.input', side_effect = ['3', '5'])
    def test_show_score(self, mock_inputs):
        """tests the access menu's ability to retrieve and calculate score statistics"""
        self.new_player.access_menu()
        self.assertEqual(self.new_player.list_of_scores, [30, 50, 100])
        self.assertEqual(self.new_player.Highscore, 100)
        self.assertEqual(self.new_player.Average, 60)

    def tearDown(self):
        """Teardown human class by closing the file"""
        if self.new_player.name == 'Test3':
            with patch('builtins.input', side_effect = ['2', 'Test1', '5']):
                self.new_player.access_menu()
        self.new_player.f.close()



if __name__=="__main__":
    unittest.main()
