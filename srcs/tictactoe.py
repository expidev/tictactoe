

class TicTacToe:
    """
        A class to represent a Tic Tac Toe game.
        Attributes:
            player_1_moves (list): Moves made by Player 1.
            player_2_moves (list): Moves made by Player 2.
            players_moves (list): All moves made by both players.
            current_player (int): The current player (1 or 2).
            board (list): The game board.
            winner (int): The winner of the game (1 or 2).
            winner_combinations (list): Possible winning combinations.
        
        Methods:
            get_board(): Displays the current state of the board.
            get_winner(): Returns the winner of the game.
            set_winner(winner): Sets the winner of the game.
            run_turn(): Executes a turn for the current player.
            check_winner(): Checks if the current player has won.
            start_game(): Starts the game loop.
    """

    def __init__(self):
        self._player_1_moves = []
        self._player_2_moves = []
        self._players_moves = []
        self._current_player = 1
        self._winner = None
        self._board = [1,2,3,4,5,6,7,8,9]
        self._winner_combinations = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,6,9], [3,5,7], [4,5,6],[7,8,9]]


    def get_board(self):
        print("\n")
        print(self._board[0],self._board[1],self._board[2], sep="|")
        print ("______")
        print (self._board[3],self._board[4],self._board[5], sep="|")
        print ("______")
        print (self._board[6],self._board[7],self._board[8], sep="|")
        print("\n")

    def get_winner(self):
        return self._winner

    def set_winner(self, winner):
        self._winner = winner

    def run_turn(self):
        move = int(input(f"Player {self._current_player}, please choose the number which indicates your move: "))

        if move not in self._board:
            print("Move unavailable, try again. \n")
            self.run_turn()
        else:
            if self._current_player == 1:
                self._player_1_moves.append(move)
                self._board[self._board.index(move)]="X"
            else:
                self._player_2_moves.append(move)
                self._board[self._board.index(move)]="O"
            self._players_moves.append(move)
            self.check_winner()
            self._current_player = 2 if self._current_player == 1 else 1


    def check_winner(self):
        for combination in self._winner_combinations:
            count = 0
            player_moves = self._player_1_moves if self._current_player == 1 else self._player_2_moves

            for number in combination:
                if number in player_moves:
                    count += 1

            if count == 3:
                self.set_winner(self._current_player)
                print(f"The winner is Player {self._current_player}!\n")

    def start_game(self):

        while len(self._players_moves) < 9 and self.get_winner() is None:
            self.get_board()
            self.run_turn()

        if self.get_winner() is None:
            print("This game is a draw.") 
