import numpy as np
from tic_tac_toe import Tic_Tac_Toe
from types import SimpleNamespace

def score(game, depth):
    if game.X_wins:
        return 10 - depth
    elif game.O_wins:
        return depth - 10
    else:
        return 0

def minimax(game, depth, isMaximizingPlayer):

    if game.is_gameover():
        return score(game, depth)
    
    depth += 1
    moves = []
    scores = []
    board = game.board_status

    # Populate the scores array, recursing as needed
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                if isMaximizingPlayer:
                    board[i][j] = 1
                else:
                    board[i][j] = -1
                scores.append(minimax(game, depth, not isMaximizingPlayer))
                moves.append([i, j])
                board[i][j] = 0

    # Do the min or the max calculation
    if isMaximizingPlayer:
        max_score_index = scores.index(max(scores))
        game.X_score = scores[max_score_index]
        game.X_choice = moves[max_score_index]
        return scores[max_score_index]
    else:
        min_score_index = scores.index(min(scores))
        game.O_score = scores[min_score_index]
        game.O_choice = moves[min_score_index]
        return scores[min_score_index]
    
if __name__ == "__main__":
    tic_tac_toe = Tic_Tac_Toe()
    human = 'X'
    computer = 'O'

    # tic_tac_toe.mainloop()
    while not tic_tac_toe.is_gameover():
        if tic_tac_toe.player_X_turns:
            # Read the human's move from terminal
            print("Enter the coordinates of your move:")
            x = int(input())
            y = int(input())
            event = SimpleNamespace(x=x, y=y)
            tic_tac_toe.click(event=event)
        else:
            minimax(tic_tac_toe, 0, True)
            event = SimpleNamespace(x=tic_tac_toe.X_choice[0], y=tic_tac_toe.X_choice[1])
            tic_tac_toe.click(event=event)
