import json
from tqdm import tqdm
from TicTacToeGame import TicTacToeGame
from TicTacToeHumanPlayer import TicTacToeHumanPlayer
from TicTacToeRandomSolver import TicTacToeRandomSolver
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver
from TicTacToeQLearningSolver import TicTacToeQLearningSolver
from TicTacToeExperimentRunner import TicTacToeExperimentRunner

def evaluate_agent(game_instance, agent, opponent, num_games=1000):
    scores = {'X': 0, 'O': 0, 'tie': 0}
    pbar = tqdm(total=num_games)
    for i in range(num_games):
        while not game_instance.is_gameover():
            if game_instance.player_X_turns:
                agent.take_turn()
            else:
                opponent.take_turn()
        if game_instance.X_wins:
            scores['X'] += 1
        elif game_instance.O_wins:
            scores['O'] += 1
        else:
            scores['tie'] += 1
        pbar.update(1)
        game_instance.play_again()
    pbar.close()
    return scores

if __name__ == '__main__':

    # Create a game instance
    game_instance = TicTacToeGame()

    # Define agents
    human_agent = TicTacToeHumanPlayer(game_instance)
    minimax_agent = TicTacToeMinimaxSolver(game_instance)
    q_learning_agent = TicTacToeQLearningSolver(game_instance)
    # q_learning_agent.load_q_tables()
    # random_solver = TicTacToeRandomSolver(game_instance)

    # Define experiment runner
    # experiment_runner = TicTacToeExperimentRunner(game_instance)
    # scores = experiment_runner.evaluate_agent(minimax_agent, human_agent, iterations=2)
    # print(scores)

    q_learning_agent.train(episodes=6000)
    q_learning_training = [evaluate_agent(game_instance, q_learning_agent, minimax_agent, num_games=100)]
    batch_train_episodes = 100
    for i in range(10):
        q_learning_agent.train(batch_train_episodes)
        scores = evaluate_agent(game_instance, q_learning_agent, minimax_agent, num_games=100)
        q_learning_training.append(scores)
        print('Q-learning vs Minimax - Batch {}: X wins: {}, O wins: {}, tie: {}'.format(i, scores['X'], scores['O'], scores['tie']))

    with open('experiments/ttt-q-learning-vs-minimax.txt', 'w') as f:
        json.dump(q_learning_training, f)