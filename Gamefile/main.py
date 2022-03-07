import Game 
def main():
    """This is to initialize the game"""
    new_game = Game.Game()
    new_game.Choose_players()
    new_game.play()
    
if __name__ == '__main__':
    """This is to give allow the main function to be called indepedently in command prompt"""
    main()

