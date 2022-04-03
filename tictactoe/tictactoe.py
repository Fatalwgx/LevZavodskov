MAP_BOARD = '_________'
PLAYER_X = 'X'
PLAYER_O = 'O'


def trace_map(cords):
    global MAP_BOARD
    MAP_BOARD = cords
    print(f'---------\n'
          f'| {cords[0]} {cords[1]} {cords[2]} |\n'
          f'| {cords[3]} {cords[4]} {cords[5]} |\n'
          f'| {cords[6]} {cords[7]} {cords[8]} |\n'
          f'---------\n')


def user_moves(string, player):
    global MAP_BOARD
    split_str = str(int(string[0]) - 1) + " " + str(int(string[2]) - 1)
    temp_board = [[MAP_BOARD[0], MAP_BOARD[1], MAP_BOARD[2]],[MAP_BOARD[3], MAP_BOARD[4],MAP_BOARD[5]], [MAP_BOARD[6], MAP_BOARD[7], MAP_BOARD[8]]]

    if temp_board[int(split_str[0])][int(split_str[2])] == '_':
        temp_board[int(split_str[0])][int(split_str[2])] = str(player)
        MAP_BOARD = f'{temp_board[0][0]}{temp_board[0][1]}{temp_board[0][2]}{temp_board[1][0]}{temp_board[1][1]}{temp_board[1][2]}{temp_board[2][0]}{temp_board[2][1]}{temp_board[2][2]}'
    else:
        print('This cell is occupied! Choose another one!')
        user_moves(user_input_move(), player)


def check_if_won(board):
    x_wins = 0
    o_wins = 0
    if abs(MAP_BOARD.count('X') - MAP_BOARD.count('O')) >= 2:
        print('Impossible')
        return True
    else:
        players = ['O', 'X']
        for player in players:
            wins = 0
            if player == board[0] and player == board[4] and player == board[8]:
                wins += 1
            elif player == board[2] and player == board[4] and player == board[6]:
                wins += 1
            elif player == board[1] and player == board[4] and player == board[7]:
                wins += 1
            elif player == board[3] and player == board[4] and player == board[5]:
                wins += 1
            elif player == board[0] and player == board[3] and player == board[6]:
                wins += 1
            elif player == board[2] and player == board[5] and player == board[8]:
                wins += 1
            elif player == board[0] and player == board[1] and player == board[2]:
                wins += 1
            elif player == board[6] and player == board[7] and player == board[8]:
                wins += 1

            if player == 'O':
                o_wins = wins
            else:
                x_wins = wins

        if '_' in board and (x_wins + o_wins) == 0:
            # print('Game not finished')
            return False
        elif '_' not in board and (x_wins + o_wins) == 0:
            trace_map(MAP_BOARD)
            print('Draw')
            return True
        elif (x_wins + o_wins) > 1:
            trace_map(MAP_BOARD)
            print('Impossible')
            return True
        elif x_wins == 1:
            trace_map(MAP_BOARD)
            print('X wins')
            return True
        elif o_wins == 1:
            trace_map(MAP_BOARD)
            print('O wins')
            return True


def user_input_cords():
    prompt = input('Enter cells: ')
    if any(char.isdigit() for char in prompt):
        print('Coordinates should be either "X", "O" or "_"')
        return user_input_cords()
    else:
        return prompt


def user_input_move():
    prompt = str(input('Enter the coordinates: '))
    if any(char.isdigit() for char in prompt):
        if int(prompt[0]) > 3 or int(prompt[2]) > 3:
            print('Coordinates should be from 1 to 3!')
            return user_input_move()
        else:
            return prompt
    else:
        print('You should enter numbers!')
        return user_input_move()


def start_game(player):
    if player == PLAYER_O:
        launch_game(PLAYER_O, PLAYER_X)
    elif player == PLAYER_X:
        launch_game(PLAYER_X, PLAYER_O)
    else:
        print('Players must be either "X" or "O"')


def launch_game(player1, player2):
    while True:
        user_moves(user_input_move(), player1)
        trace_map(MAP_BOARD)
        if win_condition():
            break
        user_moves(user_input_move(), player2)
        trace_map(MAP_BOARD)
        if win_condition():
            break


def win_condition():
    if check_if_won(MAP_BOARD):
        return True


trace_map(MAP_BOARD)
start_game(PLAYER_X)
