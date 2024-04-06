from Connect4Game import Connect4Game
from Connect4MinimaxSolver import Connect4MinimaxSolver
from Connect4RandomSolver import Connect4RandomSolver
from Connect4DefaultSolver import Connect4DefaultSolver
from Connect4ExperimentRunner import Connect4ExperimentRunner
from Connect4QLearningSolver import Connect4QLearningSolver

if __name__ == '__main__':
    game = Connect4Game()
    exp_runner = Connect4ExperimentRunner(game)
    # agent = Connect4MinimaxSolver(game, max_depth=7)
    agent = Connect4QLearningSolver(game)
    opponent = Connect4RandomSolver(game)

    # Evaluate the agent
    # scores = exp_runner.evaluate_agent(agent, opponent, iterations=10)
    # print('Agent vs Random - Minimax wins: {}, Random wins: {}, tie: {}'.format(scores['agent1'], scores['agent2'], scores['tie']))

    exp_runner.record_agent_learning_progress(agent, opponent, iterations=20, train_episodes=10000)

    # Play against the computer
    # while not game.is_gameover():
    #     game.view_board()
    #     col = int(input("Enter column: "))
    #     game.make_move(col)
    #     if game.is_gameover():
    #         break
    #     agent.take_turn()
    
    # if game.is_gameover():
    #     if game.winner == 1:
    #         print("You win!")
    #     elif game.winner == 2:
    #         print("Computer wins!")
    #     else:
    #         print("It's a draw!")