import numpy as np
from TicTacToeSolver import TicTacToeSolver

class TicTacToeQLearningSolver(TicTacToeSolver):

    def __init__(self, game_instance, learning_rate=0.5, discount_factor=0.9, exploration_rate=0.2):
        self.game = game_instance
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((3**9, 9))

    def get_state(self):
        state_id = sum([3**i * (self.game.board_status[i//3][i%3] + 1) for i in range(9)])
        return int(state_id)

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.exploration_rate:
            return np.random.choice(9)  # Explore action space
        else:
            return np.argmax(self.q_table[state])  # Exploit learned values

    def update_q_table(self, old_state, action, reward, new_state):
        old_value = self.q_table[old_state, action]
        future_max_value = np.max(self.q_table[new_state])
        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount_factor * future_max_value)
        self.q_table[old_state, action] = new_value

    def perform_action(self, action):
        logical_position = (action // 3, action % 3)
        self.append_computer_move(logical_position)
        if self.game.is_gameover():
            if self.game.X_wins:
                reward = 1
            elif self.game.O_wins:
                reward = -1
            else:
                reward = 0
            return reward, True
        return 0, False

    def train(self, episodes):
        for episode in range(episodes):
            old_state = self.get_state()
            done = False
            while not done:
                action = self.choose_action(old_state)
                reward, done = self.perform_action(action)
                new_state = self.get_state()
                self.update_q_table(old_state, action, reward, new_state)
                old_state = new_state
            self.game.play_again()

    def computer_turn(self):
        state = self.get_state()
        action = self.choose_action(state)
        self.append_computer_move((action // 3, action % 3))
        if self.game.is_gameover():
            self.game.display_gameover()