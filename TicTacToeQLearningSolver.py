import numpy as np
from TicTacToeSolver import TicTacToeSolver

class TicTacToeQLearningSolver(TicTacToeSolver):

    def __init__(self, game_instance, learning_rate=0.3, discount_factor=0.9999, exploration_rate=1, decay_rate=0.99999):
        self.game = game_instance
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate
        self.q_table_X = np.zeros((3**9, 9))
        self.q_table_O = np.zeros((3**9, 9))
        self.q_table = self.q_table_X
        self.in_training = False

    def decay_parameters(self):
        self.learning_rate = max(0.1, self.learning_rate * self.decay_rate)
        self.exploration_rate = max(0.1, self.exploration_rate * self.decay_rate)

    def get_state(self):
        state_id = sum([3**i * (self.game.board_status[i//3][i%3] + 1) for i in range(9)])
        return int(state_id)

    def choose_action(self, state):
        if self.game.player_X_turns:
            q_table = self.q_table_X
        else:
            q_table = self.q_table_O
        if np.random.uniform(0, 1) < self.exploration_rate and self.in_training:
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
                raise ValueError('No valid action found')
        return action

    def update_q_table(self, move_history, q_table, reward):
        move_history.reverse()
        next_max = -1.0
        for h in move_history:
            old_state, action, new_state = h
            qvals = q_table[old_state]
            if next_max < 0:
                qvals[action] = reward
            else:
                sample = reward + self.discount_factor * next_max
                qvals[action] = (1 - self.learning_rate) * qvals[action] + self.learning_rate * sample
            next_max = np.max(qvals)


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
        return {'X': 0, 'O': 0}, False

    def train(self, episode_range):
        self.in_training = True
        for episode in episode_range:
            X_states = []
            O_states = []
            done = False
            old_state = self.get_state()
            while not done:
                curr_state_history = X_states if self.game.player_X_turns else O_states
                action = self.choose_action(old_state)
                rewards, done = self.perform_action(action)
                new_state = self.get_state()
                curr_state_history.append((old_state, action, new_state))
                old_state = new_state
            self.update_q_table(X_states, self.q_table_X, rewards['X'])
            self.update_q_table(O_states, self.q_table_O, rewards['O'])
            self.decay_parameters(episode)
            self.game.play_again()
        print(self.exploration_rate, self.learning_rate)

    def computer_turn(self):
        self.in_training = False
        state = self.get_state()
        action = self.choose_action(state)
        self.append_computer_move((action // 3, action % 3))