import numpy as np

class Connect4Game:
    def __init__(self):
        self.board_status = np.zeros((6, 7))  # Connect 4 board is 6 rows by 7 columns
        self.player_turns = 1  # Player 1 starts
        self.gameover = False
        self.winner = None
        self.is_tie = False

    def is_gameover(self):
        # Check horizontal, vertical and diagonal lines for a win
        for row in range(6):
            for col in range(4):
                if (self.board_status[row, col:col+4] == self.player_turns).all():
                    self.gameover = True
                    self.winner = self.player_turns
                    return True
        for col in range(7):
            for row in range(3):
                if (self.board_status[row:row+4, col] == self.player_turns).all():
                    self.gameover = True
                    self.winner = self.player_turns
                    return True
        for row in range(3):
            for col in range(4):
                if (self.board_status[range(row, row+4), range(col, col+4)] == self.player_turns).all():
                    self.gameover = True
                    self.winner = self.player_turns
                    return True
                if (self.board_status[range(row, row+4), range(col+3, col-1, -1)] == self.player_turns).all():
                    self.gameover = True
                    self.winner = self.player_turns
                    return True
        # Check for a tie
        if not (self.board_status == 0).any():
            self.gameover = True
            self.is_tie = True
            return True
        return False

    def make_move(self, col):
        if self.gameover:
            raise Exception("Game Over")
        if not (self.board_status[:, col] == 0).any():
            raise Exception("Invalid Move")
        row = np.where(self.board_status[:, col] == 0)[0][-1]
        self.board_status[row, col] = self.player_turns
        if self.is_gameover():
            return self.player_turns
        self.player_turns = 3 - self.player_turns  # Switch player
        return 0  # No win yet

    def reset_board(self):
        self.board_status = np.zeros((6, 7))
        self.player_turns = 1
        self.gameover = False

    def view_board(self):
        # Print board in a human readable way
        for row in (self.board_status):
            print(' '.join('.XO'[int(cell)] for cell in row))
        print()

    def is_column_full(self, col):
        return not (self.board_status[:, col] == 0).any()

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