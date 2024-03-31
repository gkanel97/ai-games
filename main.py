from TicTacToeGame import TicTacToeGame
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver
from TicTacToeQLearningSolver import TicTacToeQLearningSolver

if __name__ == '__main__':
    training_game_instance = TicTacToeGame(use_gui=False)
    q_learning_instance = TicTacToeQLearningSolver(training_game_instance)
    q_learning_instance.train(1000)

    evaluation_game_instance = TicTacToeGame(use_gui=True)
    q_learning_instance.game = evaluation_game_instance
    q_learning_instance.ai_mainloop()
    evaluation_game_instance.mainloop()

    # minimax_instance = TicTacToeMinimaxSolver(game_instance)
    # minimax_instance.ai_mainloop()
    # game_instance.mainloop()