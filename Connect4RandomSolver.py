import random
from Connect4Solver import Connect4Solver

class Connect4RandomSolver(Connect4Solver):
        
    def __init__(self, game_instance):
        self.game = game_instance
        self.choice = None
        self.score = 0
    
    def take_turn(self):
        action = random.choice(range(7))
        while self.game.is_column_full(action):
            action = random.choice(range(7))
        self.game.make_move(action)