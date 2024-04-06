import numpy as np
from tqdm import tqdm
from Connect4Solver import Connect4Solver

_Q_TABLE_1_PATH = 'data/q_table_c4_1.pkl'
_Q_TABLE_2_PATH = 'data/q_table_c4_2.pkl'

class Connect4QLearningSolver(Connect4Solver):

    def __init__(self, game_instance, learning_rate=0.3, discount_factor=0.9999, exploration_rate=1, decay_rate=0.99999):
        self.game = game_instance
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate
        self.q_table_1 = {}
        self.q_table_2 = {}
        self.q_table = self.q_table_1
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
        if self.game.player_turns == 1:
            q_table = self.q_table_1
        else:
            q_table = self.q_table_2

        # Initialize the Q values for the state if not already present
        if state not in q_table:
            q_table[state] = np.zeros(7)

        if np.random.uniform(0, 1) < self.exploration_rate and self.in_training:
            # Choose a random action
            action = np.random.choice(7)
            while self.game.is_column_full(action):
                action = np.random.choice(7)
        else:
            # Sort the Q values of the state and choose the action with the highest Q value
            actions_sorted = sorted(
                range(len(q_table[state])), 
                key=lambda k: q_table[state][k], 
                reverse=True
            )
            action = None
            for action in actions_sorted:
                if not self.game.is_column_full(action):
                    break
            if action is None:
                raise ValueError('No valid action found')
        return action
    
    def update_q_table(self, move_history, q_table, reward):
        move_history.reverse()
        next_max = -1.0
        for h in move_history:
            state, action = h
            qvals = q_table[state]
            if next_max < 0:
                qvals[action] = reward
            else:
                sample = reward + self.discount_factor * next_max
                qvals[action] = (1 - self.learning_rate) * qvals[action] + self.learning_rate * sample
            next_max = np.max(qvals)

    def perform_action(self, action):
        if self.game.is_column_full(action):
            raise ValueError('Invalid action')
        self.game.make_move(action)
        if self.game.is_gameover():
            if self.game.winner == 1:
                rewards = (1, -1)
            elif self.game.winner == 2:
                rewards = (-1, 1)
            else:
                rewards = (0, 0)
            return rewards, True
        return (0, 0), False
    
    def train(self, episodes=1000):
        self.in_training = True
        for episode in tqdm(range(episodes)):
            states_1 = []
            states_2 = []
            done = False
            curr_state = self.get_state()
            while not done:
                curr_state_history = states_1 if self.game.player_turns == 1 else states_2
                action = self.choose_action(curr_state)
                rewards, done = self.perform_action(action)
                curr_state_history.append((curr_state, action))
                new_state = self.get_state()
                curr_state = new_state
            self.update_q_table(states_1, self.q_table_1, rewards[0])
            self.update_q_table(states_2, self.q_table_2, rewards[1])
            self.decay_parameters()
            self.game.reset_board()

    def take_turn(self):
        self.in_training = False
        state = self.get_state()
        action = self.choose_action(state)
        self.game.make_move(action)
            

        