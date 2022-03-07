import unittest
import sys
sys.path.append("Gamefile")

from HardCom import HardcomputerPlayer

""" 
This is a test that tests the class called Hardcom (Hard computer)
The method tests if the new_comp created is an instance  
"""

class TestHardComClass(unittest.TestCase):
    def setUp(self):
        """
        Set up a hardcom object
        """
        self.hard_comp = HardcomputerPlayer("Mr Robot")
    
    def test_init_default_object(self):
        """test if the object is initilize"""
        self.assertIsInstance(self.hard_comp,HardcomputerPlayer)
    def test_HardCom_name(self):
        """test if the name of the object is there"""
        self.assertEqual(self.hard_comp.name,"Mr Robot")
    
    def test_HardCom_score(self):
        """test if the score function is working"""
        self.hard_comp.plus_score(10)
        self.assertEqual(self.hard_comp.score,10)
    
    def test_HardCom_set_name(self):
        """test if the name function is working"""
        self.hard_comp.set_name("Not Mr Robot")
        self.assertEqual(self.hard_comp.name,"Not Mr Robot")
    
    def test_roll_again_true(self):
        """test if the function roll again return true""" 
        result = self.hard_comp.roll_again
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()
