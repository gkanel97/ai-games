import numpy as np

class TicTacToeGame():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self):
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))
        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

    def play_again(self):
        self.player_X_starts = True #not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))
        self.gameover = False
        self.X_wins = False
        self.O_wins = False
        self.tie = False

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def is_grid_occupied(self, logical_position):
        return not self.board_status[logical_position[0]][logical_position[1]] == 0

    def is_winner(self, player):

        player = -1 if player == 'X' else 1

        # Three in a row
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):

        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):
        # Either someone wins or all grid occupied
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        # if self.X_wins:
        #     print('X wins')
        # if self.O_wins:
        #     print('O wins')
        # if self.tie:
        #     print('Its a tie')

        return gameover
    
    def make_move(self, logical_position):
        if self.is_gameover():
            raise Exception("Game is over. Please restart the game.")
        if self.is_grid_occupied(logical_position):
            raise Exception("This grid is occupied. Please choose another grid.")
        self.board_status[logical_position[0]][logical_position[1]] = -1 if self.player_X_turns else 1
        self.player_X_turns = not self.player_X_turns
        return
        # self.gameover = self.is_gameover()
        # return self.gameover
    
    def view_board(self):
        # Print the board in a human-readable format
        print("Current Board Status:")
        print("---------------------")
        for row in self.board_status:
            print("|", end="")
            for grid in row:
                if grid == 1:
                    print(" O |", end="")
                elif grid == -1:
                    print(" X |", end="")
                else:
                    print("   |", end="")
            print("\n---------------------")
