from Connect4Game import Connect4Game
from Connect4MinimaxSolver import Connect4MinimaxSolver
from Connect4RandomSolver import Connect4RandomSolver
from Connect4DefaultSolver import Connect4DefaultSolver
from Connect4ExperimentRunner import Connect4ExperimentRunner

if __name__ == '__main__':
    game = Connect4Game()
    agent = Connect4MinimaxSolver(game)
    opponent = Connect4RandomSolver(game)
    exp_runner = Connect4ExperimentRunner(game)

    exp_runner.record_agent_learning_progress(agent, opponent, iterations=10, train_episodes=100)

    # Evaluate the agent
    # scores = exp_runner.evaluate_agent(agent, opponent, iterations=10)
    # print('Agent vs Random - Minimax wins: {}, Random wins: {}, tie: {}'.format(scores['agent1'], scores['agent2'], scores['tie']))
    
    # # Play against the computer
    # while not game.gameover:
    #     game.view_board()
    #     col = int(input("Enter column: "))
    #     game.make_move(col)
    #     if game.gameover:
    #         if game.winner == 1:
    #             print("You win!")
    #         elif game.winner == 2:
    #             print("Computer wins!")
    #         else:
    #             print("It's a draw!")
    #         break
    #     solver.take_turn()