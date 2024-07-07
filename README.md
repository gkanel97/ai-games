## Tic-tac-toe and Connect-4 AI Agents

### Table of Contents
- [Prerequisites](#prerequisites)
- [Tic-tac-toe agent](#tic-tac-toe-agent)
- [Connect-4 agent](#connect-4-agent)
- [Demonstration video](#demonstration-video)
- [Licence](#licence)

### Prerequisites

- Python 3.x
- pip

### Tic-tac-toe agent

Script: ttt.py

This script allows you to run a game of Tic Tac Toe with different types of AI agents. The types of agents available are 'minimax', 'random', 'qlearning', and 'human'. 

Usage:

python ttt.py --agent <agent_type> --opponent <opponent_type> --episodes <num_episodes> --iterations <num_iterations> --output <output_file>

Arguments:

--agent: The type of the main agent. Options are 'minimax', 'random', 'qlearning', and 'human'. Default is 'minimax'.

--opponent: The type of the opponent agent. Options are 'minimax', 'random', 'default', and 'human'. Default is 'default'.

--episodes: The number of training episodes for the Q-learning agent. This argument is ignored for other types of agents. Default is 0.

--iterations: The number of iterations to run the game. Default is 20.

--output: The name of the output file where the results will be saved. If not specified, the results will not be saved.

Note: If the agent is a Q-learning agent and the number of episodes is greater than 0, the agent will be trained for the specified number of episodes. Otherwise, the Q-tables for the agent will be loaded from a file.

### Connect-4 Agent

Script: c4.py

This script allows you to run a game of Connect 4 with different types of AI agents. The types of agents available are 'minimax', 'random', 'qlearning', and 'human'. 

Usage:

python c4.py --agent <agent_type> --opponent <opponent_type> --episodes <num_episodes> --iterations <num_iterations> --output <output_file>

Arguments:

--agent: The type of the main agent. Options are 'minimax', 'random', 'qlearning', and 'human'. Default is 'minimax'.

--opponent: The type of the opponent agent. Options are 'minimax', 'random', 'default', and 'human'. Default is 'default'.

--episodes: The number of training episodes for the Q-learning agent. This argument is ignored for other types of agents. Default is 0.

--iterations: The number of iterations to run the game. Default is 20.

--output: The name of the output file where the results will be saved. If not specified, the results will not be saved.

Note: If the agent is a Q-learning agent and the number of episodes is greater than 0, the agent will be trained for the specified number of episodes. Otherwise, the Q-tables for the agent will be loaded from a file.

### Demonstration video

[Watch the demo video here](https://drive.google.com/file/d/1TjYmWPyJSXqX6RgH1ZQe2pBgGVoIlEPu/view?usp=drive_link)

### Licence

This project is licensed under the MIT License - see the [LICENCE.md](LICENCE.md) file for details
