from TicTacToeGame import TicTacToeGame
from TicTacToeRandomSolver import TicTacToeRandomSolver
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver
from TicTacToeQLearningSolver import TicTacToeQLearningSolver

def evaluate_agent(game_instance, agent, opponent):
    agent.in_training = False
    scores = {'X': 0, 'O': 0, 'tie': 0}
    for i in range(1000):
        while not game_instance.is_gameover():
            if game_instance.player_X_turns:
                agent.computer_turn()
            else:
                opponent.computer_turn()
        if game_instance.X_wins:
            scores['X'] += 1
        elif game_instance.O_wins:
            scores['O'] += 1
        else:
            scores['tie'] += 1
        game_instance.play_again()
    return scores

def train_agent(agent, episodes_range):
    agent.in_training = True
    agent.train(episodes_range)

if __name__ == '__main__':

    # Create a game instance
    game_instance = TicTacToeGame(use_gui=False)

    # Q-learning player plays against random player
    q_learning_instance = TicTacToeQLearningSolver(game_instance)
    random_opponent = TicTacToeRandomSolver(game_instance)
    
    untrained_scores = evaluate_agent(game_instance, q_learning_instance, random_opponent)
    scores_history = [untrained_scores]
    for i in range(10):
        train_episodes = 10000
        train_agent(q_learning_instance, episodes_range=range(i*train_episodes, (i+1)*train_episodes))
        scores = evaluate_agent(game_instance, q_learning_instance, random_opponent)
        scores_history.append(scores)
        print('Q-learning vs Random - Game {}: X wins: {}, O wins: {}, tie: {}'.format(i, scores['X'], scores['O'], scores['tie']))

    # evaluation_game_instance = TicTacToeGame(use_gui=True)
    # q_learning_instance.game = evaluation_game_instance
    # q_learning_instance.ai_mainloop()
    # evaluation_game_instance.mainloop()

    # minimax_instance = TicTacToeMinimaxSolver(game_instance)
    # minimax_instance.ai_mainloop()
    # game_instance.mainloop()