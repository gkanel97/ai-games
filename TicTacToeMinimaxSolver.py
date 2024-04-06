import copy
from TicTacToeSolver import TicTacToeSolver

_REWARD = 10

class TicTacToeMinimaxSolver(TicTacToeSolver):

    def __init__(self, game_instance):
        self.game = game_instance
        self.choice = None
        self.score = 0
        
    def calculate_score(self, game, state_depth):
        if game.X_wins:
            return -_REWARD + state_depth
        elif game.O_wins:
            return _REWARD - state_depth
        else:
            return 0

    def minimax(self, game, depth, isMaximizingPlayer, alpha=-float('inf'), beta=float('inf'), use_pruning=FalseMin):

        local_game = copy.deepcopy(game)
        board = local_game.board_status

        if local_game.is_gameover():
            score = self.calculate_score(local_game, depth)
            return score, None

        depth += 1
        moves = []
        scores = []

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1 if isMaximizingPlayer else -1
                    score, _ = self.minimax(local_game, depth, not isMaximizingPlayer, alpha, beta, use_pruning)
                    scores.append(score)
                    moves.append([i, j])
                    board[i][j] = 0

                    if use_pruning:
                        if isMaximizingPlayer:
                            alpha = max(alpha, scores[-1])
                        else:
                            beta = min(beta, scores[-1])

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
        self.append_computer_move(self.choice)
        # if self.game.is_gameover():
        #     self.game.display_gameover()