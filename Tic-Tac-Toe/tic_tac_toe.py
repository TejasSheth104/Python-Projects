# snakes game on the NOKIA Phones, -_,-

board = dict()
board = { '1': '1', '2': '2', '3': '3',
          '4': '4', '5': '5', '6': '6',
          '7': '7', '8': '8', '9': '9'}

board_keys = []

for keys in board:
    board_keys.append(keys)

def draw_board(board):
    print('\t ' + board['1'] + ' | ' + board['2'] + '  | ' + board['3'])
    print('\t-- + -- + --')
    print('\t ' + board['4'] + ' | ' + board['5'] + '  | ' + board['6'])
    print('\t-- + -- + --')
    print('\t ' + board['7'] + ' | ' + board['8'] + '  | ' + board['9'])


def play_user():
    
    chance = 'X'
    count = 0

    while True:
        print('\n')
        draw_board(board)

        if count == 0:
            print('\n\n\t-#- -#- -#- -#-\n')
            print('Lets Start...')
            for keys, value in board.items():
                if board[keys] == value:
                    board[keys] = ' '
            draw_board(board)

        print('\nIts your Turn,', chance)
        move = input('Position at ? place  -> ')

        if board[move] == ' ':
            board[move] = chance 
        else:
            print('This Position is ALREADY OCCUPIED, \nplease RETRY...')
            continue


        if count >= 4:
            if (board['1'] == board['2'] and board['2'] == board['3']) or \
                (board['4'] == board['5'] and board['5'] == board['6']) or \
                (board['7'] == board['8'] and board['8'] == board['9']) or \
                (board['1'] == board['4'] and board['4'] == board['7']) or \
                (board['2'] == board['5'] and board['5'] == board['8']) or \
                (board['3'] == board['6'] and board['6'] == board['9']) or \
                (board['1'] == board['5'] and board['5'] == board['9']) or \
                (board['3'] == board['5'] and board['5'] == board['7']) or \
                (board['7'] == board['8'] and board['8'] == board['9']):
                print('Winner is - ')
                draw_board(board)
                print("\nGame Over.\n")
                break 

        if count == 9:
            print('Its a Draw...') 

        if chance == 'X':
            chance = 'O'
        else:
            chance = 'X'

        count += 1 

play_user()
