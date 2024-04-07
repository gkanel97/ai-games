import pickle
import numpy as np
from TicTacToeSolver import TicTacToeSolver

_Q_TABLE_X_PATH = 'data/q_table_X.pkl'
_Q_TABLE_O_PATH = 'data/q_table_O.pkl'

class TicTacToeQLearningSolver(TicTacToeSolver):

    def __init__(self, game_instance, learning_rate=0.3, discount_factor=0.9999, exploration_rate=1, decay_rate=0.99999):
        self.game = game_instance
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate
        self.q_table_X = {}
        self.q_table_O = {}
        self.q_table = self.q_table_X
        self.in_training = False

    def decay_parameters(self):
        self.learning_rate = max(0.1, self.learning_rate * self.decay_rate)
        self.exploration_rate = max(0.1, self.exploration_rate * self.decay_rate)

    def get_state(self):
        # Hash the board state to a unique integer
        state_id = hash(str(self.game.board_status))
        return state_id

    def choose_action(self, state):

        # Choose the suitable Q table based on the player's turn
        if self.game.player_X_turns:
            q_table = self.q_table_X
        else:
            q_table = self.q_table_O

        # Initialize the Q values for the state if not already present
        if state not in q_table:
            q_table[state] = np.zeros(9)

        if np.random.uniform(0, 1) < self.exploration_rate and self.in_training:
            # Choose a random action
            action = np.random.choice(9)
            logical_position = (action // 3, action % 3)
            while self.game.is_grid_occupied(logical_position):
                action = np.random.choice(9)
                logical_position = (action // 3, action % 3)
        else:
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
        self.game.make_move(logical_position)
        if self.game.is_gameover():
            if self.game.X_wins:
                rewards = {'X': 1, 'O': -1}
            elif self.game.O_wins:
                rewards = {'X': -1, 'O': 1}
            else:
                rewards = {'X': 0, 'O': 0}
            return rewards, True
        return {'X': 0, 'O': 0}, False

    def train(self, episodes=1000):
        self.in_training = True
        for episode in range(episodes):
            X_states = []
            O_states = []
            done = False
            curr_state = self.get_state()
            while not done:
                curr_state_history = X_states if self.game.player_X_turns else O_states
                action = self.choose_action(curr_state)
                rewards, done = self.perform_action(action)
                new_state = self.get_state()
                curr_state_history.append((curr_state, action, new_state))
                curr_state = new_state
            self.update_q_table(X_states, self.q_table_X, rewards['X'])
            self.update_q_table(O_states, self.q_table_O, rewards['O'])
            self.decay_parameters()
            self.game.play_again()
        self.in_training = False

    def save_q_tables(self):
        with open(_Q_TABLE_X_PATH, 'wb') as file:
            pickle.dump(self.q_table_X, file)
        with open(_Q_TABLE_O_PATH, 'wb') as file:
            pickle.dump(self.q_table_O, file)

    def load_q_tables(self):
        with open(_Q_TABLE_X_PATH, 'rb') as file:
            self.q_table_X = pickle.load(file)
        with open(_Q_TABLE_O_PATH, 'rb') as file:
            self.q_table_O = pickle.load(file)

    def take_turn(self):
        self.in_training = False
        state = self.get_state()
        action = self.choose_action(state)
        self.game.make_move((action // 3, action % 3))