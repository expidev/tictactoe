from tictactoe import TicTacToe

class Command:

    def exit_game(self):
        print("Exiting the game...")
        exit()


    def start_game(self):
        print("\n")
        print("Starting a new game...")
      
        game = TicTacToe()
        game.start_game()
        
        while (True):
            user_input = input("Enter 'exit' to quit or 'restart' to restart the game: ")
            if user_input == "exit":
                self.exit_game()
            elif user_input == "restart":
                self.start_game()



