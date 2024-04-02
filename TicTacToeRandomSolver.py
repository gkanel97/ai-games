import numpy as np
from TicTacToeSolver import TicTacToeSolver

class TicTacToeRandomSolver(TicTacToeSolver):

    def __init__(self, game_instance):
        self.game = game_instance
    
    def take_turn(self):
        action = np.random.choice(9)
        logical_position = (action // 3, action % 3)
        while self.game.is_grid_occupied(logical_position):
            action = np.random.choice(9)
            logical_position = (action // 3, action % 3)    
        self.append_computer_move(logical_position)