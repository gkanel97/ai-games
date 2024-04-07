import random
from TicTacToeSolver import TicTacToeSolver

class TicTacToeDefaultSolver(TicTacToeSolver):
    
    def __init__(self, game_instance):
        self.game = game_instance

    def is_winner(self, board, player):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        if board[0][0] == board[1][1] == board[2][2] == player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False
    
    def take_turn(self):

        # Find the available moves
        available_moves = []
        for i in range(3):
            for j in range(3):
                if not self.game.is_grid_occupied((i, j)):
                    available_moves.append((i, j))
        
        # Check if there are any winning moves
        local_board = self.game.board_status.copy()
        for move in available_moves:
            local_board[move[0]][move[1]] = -1 if self.game.player_X_turns else 1
            if self.is_winner(local_board, 'X' if self.game.player_X_turns else 'O'):
                logical_position = move
                self.game.make_move(logical_position)
                return
            
        # Check if there are any winning moves for the opponent
        for move in available_moves:
            local_board[move[0]][move[1]] = 1 if self.game.player_X_turns else -1
            if self.is_winner(local_board, 'O' if self.game.player_X_turns else 'X'):
                logical_position = move
                self.game.make_move(logical_position)
                return

        # If no winning moves, make a random move
        logical_position = random.choice(available_moves)
        self.game.make_move(logical_position)