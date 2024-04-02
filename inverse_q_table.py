def get_board_status(state_id):
    board_status = [[0]*3 for _ in range(3)]
    for i in range(9):
        value = (state_id // (3**i)) % 3
        board_status[i//3][i%3] = value - 1
    return board_status

def get_state_id(board_status):
    state_id = sum([3**i * (board_status[i//3][i%3] + 1) for i in range(9)])
    return int(state_id)

if __name__ == '__main__':

    while True:
        state_id = int(input())
        board_status = get_board_status(state_id)
        print(board_status)

    # while True:
    #     # Read board status from terminal
    #     board_status = []
    #     for _ in range(3):
    #         row = list(map(int, input().split()))
    #         board_status.append(row)
    #     state_id = get_state_id(board_status)
        
    #     # Get the q-values for the state
    #     with open('q_tables/q_table_400000.txt', 'r') as f:
    #         # Skip state_id lines
    #         for _ in range(state_id):
    #             f.readline()
    #         q_values = f.readline().split()
    #         q_values = list(map(float, q_values))
    #         print(q_values)