import numpy as np

class Connect4Game:
   # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self):
        self.player_X_turns = True
        self.board_status = np.zeros((6, 7))
        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

    def play_again(self):
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros((6, 7))

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def is_column_full(self, col):
        return not (self.board_status[:, col] == 0).any()

    def is_winner(self, player):

        player = -1 if player == 'X' else 1

        # Check for horizontal wins
        for row in range(6):
            for col in range(4):
                if (self.board_status[row, col:col+4] == player).all():
                    return True
        # Check for vertical wins
        for col in range(7):
            for row in range(3):
                if (self.board_status[row:row+4, col] == player).all():
                    return True
        # Check for diagonal wins
        for row in range(3):
            for col in range(4):
                if (self.board_status[range(row, row+4), range(col, col+4)] == player).all():
                    return True
                if (self.board_status[range(row, row+4), range(col+3, col-1, -1)] == player).all():
                    return True
        return False
    
    def is_tie(self):
        if not (self.board_status == 0).any():
            return True
        return False
    
    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')
        if not self.O_wins:
            self.tie = self.is_tie()
        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print("Player X wins!")
        if self.O_wins:
            print("Player O wins!")
        if self.tie:
            print("It's a tie!")
        return gameover
        
    def make_move(self, col):
        if self.gameover:
            raise Exception("Game Over")
        if not (self.board_status[:, col] == 0).any():
            raise Exception("Invalid Move")
        row = np.where(self.board_status[:, col] == 0)[0][-1]
        self.board_status[row, col] = -1 if self.player_X_turns else 1
        self.player_X_turns = not self.player_X_turns
        self.gameover = self.is_gameover()
        return self.gameover

    def view_board(self):
        # Print board in a human readable way
        for row in (self.board_status):
            print(' '.join('.XO'[int(cell)] for cell in row))
        print()

    def mainloop(self):
        while not self.gameover:
            self.view_board()
            col = int(input("Enter column: "))
            self.make_move(col)
        self.view_board()
        if self.winner == 0:
            print("It's a draw!")
        else:
            print(f"Player {self.winner} wins!")


if __name__ == '__main__':
    game = Connect4Game()
    game.mainloop()