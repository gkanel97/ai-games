from TicTacToeSolver import TicTacToeSolver

class TicTacToeHumanPlayer(TicTacToeSolver):
        
        def __init__(self, game_instance):
            self.game = game_instance
    
        def take_turn(self):
            print('Enter the row and column number separated by a space (0-2):')
            row, col = map(int, input().split())
            logical_position = (row, col)
            self.game.make_move(logical_position)
            self.game.view_board()