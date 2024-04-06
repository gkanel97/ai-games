from TicTacToeGame import TicTacToeGame
from TicTacToeHumanPlayer import TicTacToeHumanPlayer
from TicTacToeRandomSolver import TicTacToeRandomSolver
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver
from TicTacToeQLearningSolver import TicTacToeQLearningSolver
from TicTacToeExperimentRunner import TicTacToeExperimentRunner

def interactive_game(agent):
    game_instance = TicTacToeGame(use_gui=True)
    agent.ai_mainloop()
    game_instance.mainloop()

if __name__ == '__main__':

    # Create a game instance
    game_instance = TicTacToeGame(use_gui=False)

    # Define agents
    human_agent = TicTacToeRandomSolver(game_instance)
    minimax_agent = TicTacToeMinimaxSolver(game_instance)
    q_learning_agent = TicTacToeQLearningSolver(game_instance)
    q_learning_agent.load_q_tables()
    random_solver = TicTacToeRandomSolver(game_instance)

    # Define experiment runner
    experiment_runner = TicTacToeExperimentRunner(game_instance)
    scores = experiment_runner.evaluate_agent(minimax_agent, random_solver, iterations=10)
    print(scores)