import unittest
import sys
sys.path.append("Gamefile")

from EasyCom import EasyComputerPlayer
""" 
This is a test that tests the class called EasyCom
The method tests if the new_comp created is an instance  
"""

class TestEasyComClass(unittest.TestCase):
    def setUp(self):
        """
        Set up a Easy object
        """
        self.easy_comp = EasyComputerPlayer("Mrs Robot")
    
    def test_init_default_object(self):
        """test if the object is initilize"""
        self.assertIsInstance(self.easy_comp,EasyComputerPlayer)
    def test_EasyCom_name(self):
        """test if the name of the object is there"""
        self.assertEqual(self.easy_comp.name,"Mrs Robot")
    
    def test_EasyCom_score(self):
        """test if the score function is working"""
        self.easy_comp.plus_score(10)
        self.assertEqual(self.easy_comp.score,10)
    
    def test_EasyCom_set_name(self):
        """test if the name function is working"""
        self.easy_comp.set_name("Not Mrs Robot")
        self.assertEqual(self.easy_comp.name,"Not Mrs Robot")
    
    def test_roll_again_true(self):
        """test if the function roll again return true""" 
        result = self.easy_comp.roll_again
        self.assertTrue(result)
    
if __name__=="__main__":
    unittest.main()
