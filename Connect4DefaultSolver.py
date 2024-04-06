from Connect4Solver import Connect4Solver

class Connect4DefaultSolver(Connect4Solver):

    def __init__(self, game_instance):
        self.game = game_instance

    def take_turn(self):
        for player in [self.game.player_turns, 3 - self.game.player_turns]:  # Check for both players
            for col in range(7):  # Iterate over each column
                row = self.get_row(col)  # Get the row where the piece will land
                if row is None:  # Skip if the column is full
                    continue
                self.game.board_status[row, col] = player  # Simulate dropping a piece
                if self.game.is_gameover():  # Check if this results in a win
                    self.game.board_status[row, col] = 0  # Undo the move
                    return col  # Return the winning or blocking move
                self.game.board_status[row, col] = 0  # Undo the move
        return None  # No winning or blocking move found

    def get_row(self, col):
        """Return the row where a piece will land in the given column."""
        for row in range(6):
            if self.game.board_status[row, col] == 0:
                return row
        return None  # The column is full

