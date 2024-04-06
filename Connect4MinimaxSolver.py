import copy
from Connect4Solver import Connect4Solver
from datetime import datetime, timedelta

class Connect4MinimaxSolver(Connect4Solver):
    
    def __init__(self, game_instance, max_depth=4):
        self.game = game_instance
        self.choice = None
        self.score = 0
        self.history = []
        self.max_depth = max_depth
        self.stop_time = datetime.now() + timedelta(minutes=1)
    
    def calculate_score(self, game, depth):
        if game.winner == 1:
            return -10 + depth
        elif game.winner == 2:
            return 10 - depth
        else:
            return 0
        
    def minimax(self, game, depth, isMaximizingPlayer, alpha=-float('inf'), beta=float('inf'), use_pruning=True):
        # if datetime.now() > self.stop_time:
        #     return 0, None

        if game.is_gameover():
            score = self.calculate_score(game, depth)
            return score, None
        
        if depth > self.max_depth:
            return 0, None
        
        depth += 1
        moves = []
        scores = []

        for j in range(7):
            if not game.is_column_full(j):
                new_game = copy.deepcopy(game)
                space_filled = new_game.make_move(j)
                score, _ = self.minimax(new_game, depth, not isMaximizingPlayer, alpha, beta, use_pruning)
                scores.append(score)
                moves.append(j)
                game.board_status[space_filled] = 0
                # game.player_turns = 3 - game.player_turns
                
                if use_pruning:
                    if isMaximizingPlayer:
                        alpha = max(alpha, score)
                    else:
                        beta = min(beta, score)
                    
                    if beta <= alpha:
                        break
        
        if isMaximizingPlayer:
            max_score_index = scores.index(max(scores))
            score = scores[max_score_index]
            choice = moves[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            score = scores[min_score_index]
            choice = moves[min_score_index]
        
        return score, choice
        
    def take_turn(self):
        _, self.choice = self.minimax(self.game, 0, True)
        self.game.make_move(self.choice)