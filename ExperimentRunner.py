from tqdm import tqdm

class ExperimentRunner():
    
    def __init__(self, game_instance):
        self.game = game_instance

    def agent_battle(self, agent1, agent2, verbose=False):
        self.game.play_again()
        game_finished = False
        curr_agent = agent1
        while not game_finished:
            curr_agent.take_turn()
            if verbose:
                self.game.view_board()
            curr_agent = agent2 if curr_agent == agent1 else agent1
            game_finished = self.game.is_gameover()

        if self.game.X_wins:
            return 'X'
        elif self.game.O_wins:
            return 'O'
        else:
            return 'tie'
        
    def evaluate_agent(self, agent, opponent, iterations=1000, verbose=False):
        agent.in_training = False
        scores = {'X': 0, 'O': 0, 'tie': 0}
        pbar = tqdm(total=iterations, desc='Battle between agents...')
        for i in range(iterations):
            agent_battle_result = self.agent_battle(agent, opponent, verbose=verbose)
            scores[agent_battle_result] += 1
            pbar.update(1)
        pbar.close()
        print(scores)
        return scores
    
    def train_agent(self, agent, episodes, save_q_tables=False):
        agent.in_training = True
        agent.train(episodes)
        if save_q_tables:
            agent.save_q_tables()

    def record_agent_learning_progress(self, agent, opponent, iterations=20):
        untrained_scores = self.evaluate_agent(opponent, agent)
        print('Q-learning vs Random - Untrained: X wins: {}, O wins: {}, tie: {}'.format(untrained_scores['X'], untrained_scores['O'], untrained_scores['tie']))
        scores_history = [untrained_scores]
        for i in range(iterations):
            train_episodes = 10000
            self.train_agent(agent, episodes=train_episodes)
            scores = self.evaluate_agent(opponent, agent)
            scores_history.append(scores)
            print('Q-learning vs Random - Game {}: X wins: {}, O wins: {}, tie: {}'.format(i, scores['X'], scores['O'], scores['tie']))
        return scores_history
        
