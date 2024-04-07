import numpy as np
from Connect4Solver import Connect4Solver

REWARD = 10

class Connect4MinimaxSolver(Connect4Solver):
    
    def __init__(self, game_instance, max_depth=4, use_pruning=True):
        self.game = game_instance
        self.choice = None
        self.score = 0
        self.history = {}
        self.max_depth = max_depth
        self.use_pruning = use_pruning
    
    def calculate_score(self, depth):
        if self.game.X_wins:
            return -REWARD + depth
        elif self.game.O_wins:
            return REWARD - depth
        else:
            return 0
        
    def potential_wins(self, board, player):
        count = 0
        # Check rows for potential winning lines
        for row in range(6):
            for col in range(4):
                if (board[row][col] == player or board[row][col] == 0) and \
                (board[row][col+1] == player or board[row][col+1] == 0) and \
                (board[row][col+2] == player or board[row][col+2] == 0) and \
                (board[row][col+3] == player or board[row][col+3] == 0):
                    count += 1

        # Check columns for potential winning lines
        for col in range(7):
            for row in range(3):
                if (board[row][col] == player or board[row][col] == 0) and \
                (board[row+1][col] == player or board[row+1][col] == 0) and \
                (board[row+2][col] == player or board[row+2][col] == 0) and \
                (board[row+3][col] == player or board[row+3][col] == 0):
                    count += 1

        # Check diagonals (bottom left to top right) for potential winning lines
        for row in range(3):
            for col in range(4):
                if (board[row][col] == player or board[row][col] == 0) and \
                (board[row+1][col+1] == player or board[row+1][col+1] == 0) and \
                (board[row+2][col+2] == player or board[row+2][col+2] == 0) and \
                (board[row+3][col+3] == player or board[row+3][col+3] == 0):
                    count += 1

        # Check diagonals (top left to bottom right) for potential winning lines
        for row in range(3, 6):
            for col in range(4):
                if (board[row][col] == player or board[row][col] == 0) and \
                (board[row-1][col+1] == player or board[row-1][col+1] == 0) and \
                (board[row-2][col+2] == player or board[row-2][col+2] == 0) and \
                (board[row-3][col+3] == player or board[row-3][col+3] == 0):
                    count += 1
        return count
        
    def minimax(self, depth, isMaximizingPlayer, alpha=-float('inf'), beta=float('inf')):

        if self.game.is_gameover():
            return self.calculate_score(depth)
        
        if depth > self.max_depth:
            possible_wins = self.potential_wins(self.game.board_status, 1 if isMaximizingPlayer else -1)
            possible_losses = self.potential_wins(self.game.board_status, -1 if isMaximizingPlayer else 1)
            return possible_wins - possible_losses
        
        depth += 1
        moves = []
        scores = []
        board = self.game.board_status

        for j in range(7):
            if not self.game.is_column_full(j):
                i = np.where(board[:, j] == 0)[0][-1]
                board[i, j] = 1 if isMaximizingPlayer else -1
                scores.append(self.minimax(depth, not isMaximizingPlayer, alpha, beta))
                moves.append(j)
                board[i, j] = 0
                
                if self.use_pruning:
                    if isMaximizingPlayer:
                        alpha = max(alpha, scores[-1])
                    else:
                        beta = min(beta, scores[-1])
                    
                    if beta <= alpha:
                        break
        
        if isMaximizingPlayer:
            max_score_index = scores.index(max(scores))
            self.score = scores[max_score_index]
            self.choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            self.score = scores[min_score_index]
            self.choice = moves[min_score_index]
            return scores[min_score_index]
        
    def take_turn(self):
        self.minimax(0, True)
        self.game.make_move(self.choice)