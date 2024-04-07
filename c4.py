import argparse

from Connect4Game import Connect4Game
from ExperimentRunner import ExperimentRunner
from Connect4HumanPlayer import Connect4HumanPlayer
from Connect4DefaultSolver import Connect4DefaultSolver
from Connect4RandomSolver import Connect4RandomSolver
from Connect4MinimaxSolver import Connect4MinimaxSolver
from Connect4QLearningSolver import Connect4QLearningSolver

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='minimax', help='Main agent')
    parser.add_argument('--opponent', type=str, default='default', help='Opponent agent')
    parser.add_argument('--episodes', type=int, default=0, help='Number of training episodes')
    parser.add_argument('--iterations', type=int, default=20, help='Number of iterations')
    parser.add_argument('--output', type=str, default=None, help='Output file')
    parser.add_argument('--use_pruning', type=bool, default=True, help='Use pruning in minimax')
    args = parser.parse_args()

    if args.agent == 'minimax':
        agent = Connect4MinimaxSolver
    elif args.agent == 'random':
        agent = Connect4RandomSolver
    elif args.agent == 'qlearning':
        agent = Connect4MinimaxSolver
        # agent = Connect4QLearningSolver
    elif args.agent == 'human':
        agent = Connect4HumanPlayer
    else:
        raise ValueError('Invalid agent')
    
    if args.opponent == 'minimax':
        opponent = Connect4MinimaxSolver
    elif args.opponent == 'random':
        opponent = Connect4RandomSolver
    elif args.opponent == 'default':
        opponent = Connect4DefaultSolver
    elif args.opponent == 'human':
        opponent = Connect4HumanPlayer
    else:
        raise ValueError('Invalid opponent')
    
    episodes = args.episodes
    iterations = args.iterations
    output_file = args.output
    verbose = 'human' in [args.agent, args.opponent]

    # Create a game instance
    game_instance = Connect4Game()

    # Create an experiment runner
    exp_runner = ExperimentRunner(game_instance)

    if args.agent == 'qlearning1':
        if episodes > 0:
            agent_instance = agent(game_instance)
            exp_runner.train_agent(agent_instance, episodes, save_q_tables=True)
        else:
            agent_instance = agent(game_instance)
            agent_instance.load_q_tables()
    else:
        agent_instance = agent(game_instance)
    opponent_instance = opponent(game_instance)

    exp_runner.evaluate_agent(agent_instance, opponent_instance, iterations=iterations, verbose=verbose)