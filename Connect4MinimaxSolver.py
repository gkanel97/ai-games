import copy
import numpy as np
from Connect4Solver import Connect4Solver
from datetime import datetime, timedelta

class Connect4MinimaxSolver(Connect4Solver):
    
    def __init__(self, game_instance, max_depth=4):
        self.game = game_instance
        self.choice = None
        self.score = 0
        self.history = []
        self.max_depth = 4
        self.stop_time = datetime.now() + timedelta(minutes=1)
    
    def calculate_score(self, depth):
        if self.game.player_turns == 1:
            return -10 + depth
        elif self.game.player_turns == 2:
            return 10 - depth
        else:
            return 0
        
    def minimax(self, game, depth, isMaximizingPlayer, alpha=-float('inf'), beta=float('inf'), use_pruning=True):
        # if datetime.now() > self.stop_time:
        #     return 0, None

        if game.is_gameover():
            # self.history.append(game.board_status)
            score = self.calculate_score(depth)
            return score, None
        
        if depth > self.max_depth:
            return 0, None
        
        depth += 1
        moves = []
        scores = []
        board = game.board_status
        prune = False
        
        for i in range(6):
            if prune:
                break
            for j in range(7):
                if board[i][j] == 0:
                    new_game = copy.deepcopy(game)
                    new_game.make_move(j)
                    score, _ = self.minimax(new_game, depth, not isMaximizingPlayer, alpha, beta, use_pruning)
                    scores.append(score)
                    moves.append([i, j])
                    board[i][j] = 0
                    
                    if use_pruning:
                        if isMaximizingPlayer:
                            alpha = max(alpha, score)
                        else:
                            beta = min(beta, score)
                        
                        if beta <= alpha:
                            prune = True
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
        self.game.make_move(self.choice[1])