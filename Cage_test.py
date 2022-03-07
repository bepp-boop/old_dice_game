import unittest
import sys
sys.path.append("Gamefile")

import Cage

""" 
This is a test that tests the class called cage  
"""

class TestCageClass(unittest.TestCase):

    def setUp(self):
        """Set up cage.box object"""
        self.new_box = Cage.Box()
        
    def test_init_default_object(self):
        """ The method tests if the box created is an instance """
        self.assertIsInstance(self.new_box,Cage.Box)

    def test_add_dice_value(self):
        """ The method tests if values are added to the box """
        self.new_box.add_dice_value(6)
        self.assertEqual(self.new_box.value, 6)

    def test_reset(self):
        """ The method tests if the value is reset to 0 when 1 is rolled """
        self.new_box.reset()
        self.assertEqual(self.new_box.value,0)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
