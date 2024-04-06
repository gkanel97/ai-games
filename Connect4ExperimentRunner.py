from tqdm import tqdm

class Connect4ExperimentRunner():
    
    def __init__(self, game_instance):
        self.game = game_instance

    def agent_battle(self, agent1, agent2):
        self.game.reset_board()
        game_finished = False
        while not game_finished:
            agent1.take_turn() if self.game.player_turns == 1 else agent2.take_turn()
            game_finished = self.game.is_gameover()

        if self.game.winner == 1:
            return 'agent1'
        elif self.game.winner == 2:
            return 'agent2'
        else:
            return 'tie'
        
    def evaluate_agent(self, agent, opponent, iterations=100):
        scores = {'agent1': 0, 'agent2': 0, 'tie': 0}
        pbar = tqdm(total=iterations)
        for i in range(iterations):
            agent_battle_result = self.agent_battle(agent, opponent)
            scores[agent_battle_result] += 1
            pbar.update(1)
        pbar.close()
        print(f'Agent vs Default - Minimax wins: {scores["agent1"]}, Default wins: {scores["agent2"]}, tie: {scores["tie"]}')
        return scores
    
    def train_agent(self, agent, episodes, save_q_tables=False):
        agent.in_training = True
        agent.train(episodes)
        if save_q_tables:
            agent.save_q_tables()

    def record_agent_learning_progress(self, agent, opponent, iterations=20, train_episodes=10000):
        untrained_scores = self.evaluate_agent(opponent, agent)
        print('Q-learning vs Random - Untrained: agent1 wins: {}, agent2 wins: {}, tie: {}'.format(untrained_scores['agent1'], untrained_scores['agent2'], untrained_scores['tie']))
        scores_history = [untrained_scores]
        for i in range(iterations):
            self.train_agent(agent, episodes=train_episodes)
            scores = self.evaluate_agent(opponent, agent)
            scores_history.append(scores)
            print('Q-learning vs Random - Game {}: agent1 wins: {}, agent2 wins: {}, tie: {}'.format(i, scores['agent1'], scores['agent2'], scores['tie']))
        return scores_history
        