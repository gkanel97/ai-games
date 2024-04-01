import numpy as np
from TicTacToeSolver import TicTacToeSolver
from tqdm import tqdm

class TicTacToeQLearningSolver(TicTacToeSolver):

    def __init__(self, game_instance, learning_rate=0.9, discount_factor=0.99, exploration_rate=0.5, decay_rate=1e-6):
        self.game = game_instance
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate
        self.q_table_X = np.zeros((3**9, 9))
        self.q_table_O = np.zeros((3**9, 9))
        self.q_table = self.q_table_X

    def decay_parameters(self, iteration_count):
        self.learning_rate *= np.exp(-self.decay_rate * iteration_count)
        self.exploration_rate *= np.exp(-self.decay_rate * iteration_count)

    def get_state(self):
        state_id = sum([3**i * (self.game.board_status[i//3][i%3] + 1) for i in range(9)])
        return int(state_id)

    def choose_action(self, state):
        if self.game.player_X_turns:
            q_table = self.q_table_X
        else:
            q_table = self.q_table_O
        if np.random.uniform(0, 1) < self.exploration_rate:
            # Explore action space
            action = np.random.choice(9)
            logical_position = (action // 3, action % 3)
            while self.game.is_grid_occupied(logical_position):
                action = np.random.choice(9)
                logical_position = (action // 3, action % 3)
        else:
            # Exploit learned values
            # Sort the Q values of the state and choose the action with the highest Q value
            actions_sorted = sorted(
                range(len(q_table[state])), 
                key=lambda k: q_table[state][k], 
                reverse=True
            )
            action = None
            for action in actions_sorted:
                logical_position = (action // 3, action % 3)
                if not self.game.is_grid_occupied(logical_position):
                    break
            if action is None:
                print('Error: No valid action found')
        return action

    def update_q_table(self, old_state, action, new_state, player_X_turns, rewards):
        if player_X_turns:
            q_table = self.q_table_X
            reward = rewards['X']
        else:
            q_table = self.q_table_O
            reward = rewards['O']
        old_estimate = q_table[old_state, action]
        future_max_value = np.max(q_table[new_state])
        sample = reward + self.discount_factor * future_max_value
        new_estimate = (1 - self.learning_rate) * old_estimate + self.learning_rate * sample
        q_table[old_state, action] = new_estimate

    def perform_action(self, action):
        logical_position = (action // 3, action % 3)
        self.append_computer_move(logical_position)
        if self.game.is_gameover():
            if self.game.X_wins:
                rewards = {'X': 1, 'O': -1}
            elif self.game.O_wins:
                rewards = {'X': -1, 'O': 1}
            else:
                rewards = {'X': 0, 'O': 0}
            return rewards, True
        return 0, False

    def train(self, episodes):
        for episode in tqdm(range(episodes)):
        # for episode in range(episodes):
            states = []
            done = False
            old_state = self.get_state()
            while not done:
                self.q_table = self.q_table_X if self.game.player_X_turns else self.q_table_O
                action = self.choose_action(old_state)
                rewards, done = self.perform_action(action)
                new_state = self.get_state()
                states.append((old_state, action, new_state, not self.game.player_X_turns))
                old_state = new_state
            for old_state, action, new_state, player_X_turns in states:
                self.update_q_table(old_state, action, new_state, player_X_turns, rewards)
            self.game.play_again()
            self.decay_parameters(episode)
        with open(f'q_tables/q_table_X_{episode}.txt', 'w') as f:
            np.savetxt(f, self.q_table_X, fmt='%f')
        with open(f'q_tables/q_table_O_{episode}.txt', 'w') as f:
            np.savetxt(f, self.q_table_O, fmt='%f')

    def computer_turn(self):
        self.exploration_rate = 0
        state = self.get_state()
        action = self.choose_action(state)
        self.append_computer_move((action // 3, action % 3))
        if self.game.is_gameover():
            self.game.display_gameover()