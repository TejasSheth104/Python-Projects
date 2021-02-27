
# import random

# board = dict()
# board = { '1': '1', '2': '2', '3': '3',
#           '4': '4', '5': '5', '6': '6',
#           '7': '7', '8': '8', '9': '9'}

# position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# board_keys = []

# for keys in board:
#     board_keys.append(keys)

# def draw_board(board):
#     print('\t ' + board['1'] + ' | ' + board['2'] + '  | ' + board['3'])
#     print('\t-- + -- + --')
#     print('\t ' + board['4'] + ' | ' + board['5'] + '  | ' + board['6'])
#     print('\t-- + -- + --')
#     print('\t ' + board['7'] + ' | ' + board['8'] + '  | ' + board['9'])


# def clear(count):
#     if count == 0:
#         print('\n\n\t-#- -#- -#- -#-\n')
#         print('Lets Start...')
#         for keys, value in board.items():
#             if board[keys] == value:
#                 board[keys] = ' '
#         draw_board(board)


# def winning_condition(count, chance):
#     if count >= 4:
#         if (board['1'] == board['2'] and board['2'] == board['3']) or \
#             (board['4'] == board['5'] and board['5'] == board['6']) or \
#             (board['7'] == board['8'] and board['8'] == board['9']) or \
#             (board['1'] == board['4'] and board['4'] == board['7']) or \
#             (board['2'] == board['5'] and board['5'] == board['8']) or \
#             (board['3'] == board['6'] and board['6'] == board['9']) or \
#             (board['1'] == board['5'] and board['5'] == board['9']) or \
#             (board['3'] == board['5'] and board['5'] == board['7']) or \
#             (board['7'] == board['8'] and board['8'] == board['9']):
#             print('\nWinner is - ', chance)
#             draw_board(board)
#             print("\nGame Over.\n")
#             return 1
#         else:
#             return 0


# def switch(chance):
#     if chance == 'X':
#         chance = 'O'
#     else:
#         chance = 'X'
#     return chance


# def play_user_v_user():
#     chance = 'X'
#     count = 0
#     while True:
#         print('\n')
#         draw_board(board)
#         clear(count)
#         print('\nIts your Turn,', chance)
#         move = input('Position at ? place  -> ')
#         if board[move] == ' ':
#             board[move] = chance 
#         else:
#             print('This Position is ALREADY OCCUPIED, \nplease RETRY...')
#             continue
#         check = winning_condition(count, chance)
#         if check == 1:
#             break
#         if count == 9:
#             print('Its a TIE...') 
#         chance = switch(chance)
#         count += 1 


# def play_user_v_comp():
#     chance = 'X'
#     count = 0
#     while True:
#         move = ''
#         print('\n')
#         draw_board(board)
#         clear(count)
#         print('\nIts your Turn,', chance)
#         if chance == 'O':
#             print('Its Computers Turn.')
#             move = random.choice(position)
#             print('Computers Move - ', move)
#         else:
#             move = input('Position at ? place  -> ')
#         if board[move] == ' ':
#             board[move] = chance 
#         else:
#             print('This Position is ALREADY OCCUPIED, \nplease RETRY...')
#             continue
#         check = winning_condition(count, chance)
#         if check == 1:
#             break
#         if count == 9:
#             print('Its a TIE...') 
#         chance = switch(chance)
#         count += 1


# def play_comp_v_comp():
#     chance = 'X'
#     count = 0
#     while True:
#         move = ''
#         print('\n')
#         draw_board(board)
#         clear(count)
#         print('\nIts your Turn,', chance)
#         if chance == 'O':
#             print('Its Computer2 Turn.')
#             move = random.choice(position)
#             print('Computer2 Move - ', move)
#         else:
#             print('Its Computer1 Turn.')
#             move = random.choice(position)
#             print('Computer1 Move - ', move)
#         if board[move] == ' ':
#             board[move] = chance 
#         else:
#             print('This Position is ALREADY OCCUPIED, \nplease RETRY...')
#             continue
#         check = winning_condition(count, chance)
#         if check == 1:
#             break
#         if count == 9:
#             print('Its a TIE...') 
#         chance = switch(chance)
#         count += 1

# while True:
#     print('\n\tTIC TAC TOE.')
#     print('\t0. EXIT')
#     print('\n\tPLAY - ')
#     print('\t1. PLAYER1 vs COMPUTER')
#     print('\t2. PLAYER1 vs PLAYER2')
#     print('\t3. COMPUTER1 vs COMPUTER2')
#     try:
#         choice = int(input('Enter - '))
#     except:
#         print('Invalid, Try again')
#         continue
#     if choice == 0:
#         break
#     elif choice == 1:
#         play_user_v_comp()
#     elif choice == 2:
#         play_user_v_user()
#     elif choice == 3:
#         play_comp_v_comp()
    
# print('THANK YOU ALL.')
