from Connect4Solver import Connect4Solver

class Connect4HumanPlayer(Connect4Solver):
        
        def __init__(self, game_instance):
            self.game = game_instance
    
        def take_turn(self):
            print('Enter the column number (0-6):')
            col = int(input())
            self.game.make_move(col)
            # self.game.view_board()