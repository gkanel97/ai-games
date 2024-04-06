import numpy as np

class Connect4Game:
    def __init__(self):
        self.board_status = np.zeros((6, 7))  # Connect 4 board is 6 rows by 7 columns
        self.player_turns = 1  # Player 1 starts
        self.gameover = False
        self.winner = None
        self.tie = False

    def is_winner(self, player):
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
        player_1_wins = self.is_winner(1)
        if player_1_wins:
            self.winner = 1
        player_2_wins = self.is_winner(2)
        if player_2_wins:
            self.winner = 2
        self.tie = self.is_tie()
        self.gameover = player_1_wins or player_2_wins or self.tie
        return self.gameover

    def make_move(self, col):
        if self.gameover:
            raise Exception("Game Over")
        if not (self.board_status[:, col] == 0).any():
            raise Exception("Invalid Move")
        row = np.where(self.board_status[:, col] == 0)[0][-1]
        self.board_status[row, col] = self.player_turns
        # if self.is_gameover():
        #     return self.player_turns
        self.player_turns = 3 - self.player_turns  # Switch player
        return (row, col)
        # return 0  # No win yet

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