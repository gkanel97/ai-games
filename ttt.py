import json
import argparse

from TicTacToeGame import TicTacToeGame
from TicTacToeHumanPlayer import TicTacToeHumanPlayer
from TicTacToeDefaultSolver import TicTacToeDefaultSolver
from TicTacToeRandomSolver import TicTacToeRandomSolver
from TicTacToeMinimaxSolver import TicTacToeMinimaxSolver
from TicTacToeQLearningSolver import TicTacToeQLearningSolver
from TicTacToeExperimentRunner import TicTacToeExperimentRunner

def interactive_game(agent):
    game_instance = TicTacToeGame(use_gui=True)
    agent.ai_mainloop()
    game_instance.mainloop()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='minimax', help='Main agent')
    parser.add_argument('--opponent', type=str, default='default', help='Opponent agent')
    parser.add_argument('--episodes', type=int, default=0, help='Number of training episodes')
    parser.add_argument('--iterations', type=int, default=20, help='Number of iterations')
    parser.add_argument('--output', type=str, default=None, help='Output file')
    parser.add_argument('--user_pruning', type=bool, default=True, help='Use pruning in minimax')
    args = parser.parse_args()

    if args.agent == 'minimax':
        agent = TicTacToeMinimaxSolver
    elif args.agent == 'random':
        agent = TicTacToeRandomSolver
    elif args.agent == 'qlearning':
        agent = TicTacToeQLearningSolver
    else:
        raise ValueError('Invalid agent')
    
    if args.opponent == 'minimax':
        opponent = TicTacToeMinimaxSolver
    elif args.opponent == 'random':
        opponent = TicTacToeRandomSolver
    elif args.opponent == 'default':
        opponent = TicTacToeDefaultSolver
    elif args.opponent == 'human':
        opponent = TicTacToeHumanPlayer
    else:
        raise ValueError('Invalid opponent')
    
    episodes = args.episodes
    iterations = args.iterations
    output_file = args.output

    # Create a game instance
    game_instance = TicTacToeGame(use_gui=True if args.opponent == 'human' else False)

    # Create an experiment runner
    exp_runner = TicTacToeExperimentRunner(game_instance)

    if args.agent == 'qlearning':
        if episodes > 0:
            agent_instance = agent(game_instance)
            exp_runner.train_agent(agent_instance, episodes, save_q_tables=True)
        else:
            agent_instance = agent(game_instance)
            agent_instance.load_q_tables()
    else:
        agent_instance = agent(game_instance)
    opponent_instance = opponent(game_instance)

    # Evaluate the agent
    if args.opponent == 'human':
        interactive_game(agent(game_instance))
        exit()
    else:
        scores = exp_runner.evaluate_agent(agent(game_instance), opponent(game_instance), iterations=iterations)
        if output_file:
            with open(output_file, 'a') as f:
                json.dump(scores, f)
        else:
            print(scores)