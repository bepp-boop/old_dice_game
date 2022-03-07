"""
Cage acts as the place where the score is stored before it goes into the actual score
"""
class Box:
    def __init__(self):
        """Initializes the class"""
        self.value = 0

    def reset(self):
        """reset the box (when a 1 is rolled or after the score is stored)"""
        self.value = 0

    def add_dice_value(self, dice_value):
        """Adds value into the cage"""
        self.value += dice_value