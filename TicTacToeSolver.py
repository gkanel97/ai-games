class TicTacToeSolver():

    def __init__(self, game_instance):
        self.game = game_instance

    def append_computer_move(self, logical_position):
        if self.game.player_X_turns:
            move = -1
            if self.game.use_gui:
                self.game.draw_X(logical_position)
        else:
            move = 1
            if self.game.use_gui:
                self.game.draw_O(logical_position)
        self.game.board_status[logical_position[0]][logical_position[1]] = move
        self.game.player_X_turns = not self.game.player_X_turns
        # if self.game.use_gui:
        #     self.game.draw_O(logical_position)
        # self.game.board_status[logical_position[0]][logical_position[1]] = 1

    def take_turn(self):
        pass

    # Write a new version of mainloop to include the computer turn
    # The computer is always player O
    def ai_mainloop(self):
        if not self.game.is_gameover():
            if not self.game.player_X_turns:
                self.take_turn()
        self.game.window.after(1000, self.ai_mainloop)  # Call this method again after 1 second