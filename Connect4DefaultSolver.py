import copy
import random
from Connect4Solver import Connect4Solver

class Connect4DefaultSolver(Connect4Solver):

    def __init__(self, game_instance):
        self.game = game_instance

    def detect_game_ending_move(self, player):
        """Return a winning or blocking move for the given player."""
        local_game = copy.deepcopy(self.game)  # Create a copy of the game
        for col in range(7):  # Iterate over each column
            row = self.get_row(col)  # Get the row where the piece will land
            if row is None:  # Skip if the column is full
                continue
            local_game.board_status[row, col] = player  # Simulate dropping a piece
            if local_game.is_gameover():  # Check if this results in a win
                local_game.board_status[row, col] = 0  # Undo the move
                return col  # Return the winning or blocking move
            local_game.board_status[row, col] = 0  # Undo the move
        return None  # No winning or blocking move found

    def take_turn(self):
        # Check for a winning move
        move = self.detect_game_ending_move(-1 if self.game.player_X_turns else 1)
        if move is not None:
            self.game.make_move(move)
            return
        # Check for a blocking move
        move = self.detect_game_ending_move(1 if self.game.player_X_turns else -1)
        if move is not None:
            self.game.make_move(move)
            return
        # Choose a random move
        move = random.choice(range(7))
        while self.game.is_column_full(move):
            move = random.choice(range(7))
        self.game.make_move(move)

    def get_row(self, col):
        """Return the row where a piece will land in the given column."""
        for row in reversed(range(6)):
            if self.game.board_status[row, col] == 0:
                return row
        return None  # The column is full

