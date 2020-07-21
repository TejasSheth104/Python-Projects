# snakes game on the NOKIA Phones, -_,-

board = dict()
board = { '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

def draw_board():
    print('\t ' + board['1'] + ' | ' + board['2'] + '  | ' + board['3'])
    print('\t-- + -- + --')
    print('\t ' + board['4'] + ' | ' + board['5'] + '  | ' + board['6'])
    print('\t-- + -- + --')
    print('\t ' + board['7'] + ' | ' + board['8'] + '  | ' + board['9'])


def play():
    draw_board()
    action = 'X'
    while True:
        


