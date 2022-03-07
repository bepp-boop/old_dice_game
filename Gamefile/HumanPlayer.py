"""
This class represents the human player, which extends the player class
"""
from Player import P_Player
import os

class Human(P_Player):
    def __init__(self, name):
        """initialise the human player"""
        super(Human,self).__init__(name)
        self.f = open('Saves/{}.txt'.format(self.name),'a+')
    
    def roll_again(self,box):
        """Asks the human player, if they want to keep rolling."""
        while True:
            human_choice = int(input("Choice 1 to roll again and 0 to hold" ))
            if human_choice == 1:
                return True
            if human_choice == 2:
                self.access_menu()
            else:
                return False

    def access_menu(self):
        """creates the access menu, which allows a player to cheat, change their name (which will change the name on their savefile), see statistics (by accessing their save file), quit the game or resume the game"""
        
        while True:
            print("""Player menu: 
                    - Press 1 to cheat
                    - Press 2 to change username
                    - Press 3 to see statistics
                    - Press 4 to quit the game
                    - Press 5 to resume the game""")
            menu_choice = int(input(" "))

            if menu_choice == 1:
                point_add = int(input("How much score do you want to gain "))
                self.plus_score(point_add)

            if menu_choice == 2:
                new_name = str(input("Change your username "))
                try:
                    self.f.close()
                    os.rename('Saves/{}.txt'.format(self.name), 'Saves/{}.txt'.format(new_name))
                    self.f = open('Saves/{}.txt'.format(new_name),'a+')
                    print("File name changed!")
                except FileExistsError:
                    new_name = input("Username already in use. Choose another username ")
                    os.rename('Saves/{}.txt'.format(self.name), 'Saves/{}.txt'.format(new_name))
                    self.f = open('Saves/{}.txt'.format(new_name),'a+')
                    print("File name changed!")
                self.set_name(new_name)

            if menu_choice == 3:
                self.list_of_scores = []
                self.f.close()
                self.f = open('Saves/{}.txt'.format(self.name),'r')
                Scores = self.f.readlines()
                for x in Scores:
                    score = int(x)
                    self.list_of_scores.append(score)
                self.Highscore = 0
                self.Average = 0
                for x in self.list_of_scores:
                    self.Average = self.Average + x
                    if x > self.Highscore:
                        self.Highscore = x
                try:
                    self.Average = self.Average/len(self.list_of_scores)
                except ZeroDivisionError:
                    self.Average = 0
                print("List of scores: ", self.list_of_scores)
                print("Highscore: ", self.Highscore)
                print("Average: ", self.Average)
                self.f.close()
                self.f = open('Saves/{}.txt'.format(self.name),'a+')
                
            if menu_choice == 4:
                self.f.write("{} \n".format(str(self.score)))
                self.f.close()
                quit()
            if menu_choice == 5:
                return False

    def __del__(self):
        """closes the file"""
        if self.f.closed is not True:
            self.f.close()

