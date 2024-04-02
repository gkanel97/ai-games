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
        player_symbol = -1 if self.game.player_X_turns else 1
        for move in available_moves:
            local_board[move[0]][move[1]] = player_symbol
            if self.is_winner(local_board, player_symbol):
                logical_position = move
                self.append_computer_move(logical_position)
                return
            
        # Check if there are any winning moves for the opponent
        opponent_symbol = 1 if self.game.player_X_turns else -1
        for move in available_moves:
            local_board[move[0]][move[1]] = opponent_symbol
            if self.is_winner(local_board, opponent_symbol):
                logical_position = move
                self.append_computer_move(logical_position)
                return

        # If no winning moves, make a random move
        logical_position = random.choice(available_moves)
        self.append_computer_move(logical_position)