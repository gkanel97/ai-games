import numpy as np
from tic_tac_toe import Tic_Tac_Toe
    
if __name__ == "__main__":
    game_instance = Tic_Tac_Toe()
    game_instance.ai_mainloop()
    game_instance.window.mainloop()
