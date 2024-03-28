from TicTacToeGame import TicTacToeGame
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver

if __name__ == '__main__':
    game_instance = TicTacToeGame()
    minimax_instance = TicTacToeMinimaxSolver(game_instance)
    minimax_instance.ai_mainloop()
    game_instance.mainloop()