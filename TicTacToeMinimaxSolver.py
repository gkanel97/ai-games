from TicTacToeSolver import TicTacToeSolver

class TicTacToeMinimaxSolver(TicTacToeSolver):

    def __init__(self, game_instance):
        self.game = game_instance
        self.choice = None
        self.score = 0
        
    def calculate_score(self, depth):
        if self.game.X_wins:
            return -10 + depth
        elif self.game.O_wins:
            return 10 - depth
        else:
            return 0

    def minimax(self, depth, isMaximizingPlayer):
        if self.game.is_gameover():
            self.score = 0
            self.choice = None
            return self.calculate_score(depth)

        depth += 1
        moves = []
        scores = []
        board = self.game.board_status

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    if isMaximizingPlayer:
                        board[i][j] = 1
                    else:
                        board[i][j] = -1
                    scores.append(self.minimax(depth, not isMaximizingPlayer))
                    moves.append([i, j])
                    board[i][j] = 0

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
        
    def computer_turn(self):
        self.minimax(0, True)
        self.append_computer_move(self.choice)
        if self.game.is_gameover():
            self.game.display_gameover()