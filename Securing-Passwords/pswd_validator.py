# enter your password to verify its strength
# check of Capital letters, Symbols, Numbers
#
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "\\!@#$%^&*()_-;|:,.><?/"


def condition(count_symbols, count_number, count_letter):
    if count_symbols < 1: print('Use More Special Characters.')
    if count_number <= (int(len(pswd) / 3)): print('Use More Numerical Characters.')
    if count_letter <= (int(len(pswd) / 3)): print('Use More Letters.')


letter, number, symbol = 0, 0, 0
pswd = input('Enter your Password - ')
if len(pswd) > 7:
    for piece in pswd:
        if piece in letters:
            letter += 1
        elif piece in numbers:
            number += 1
        elif piece in symbols:
            symbol += 1
        else:
            print('Character Doesnt Exist.')

if symbol > 1 and number > (int(len(pswd)/3)) and letter > (int(len(pswd)/3)):
    print('SUCCESS..!\nYour Password is Valid - ')
    if letter + number + symbol < 10:
        print('\tBut WEAK.')
        condition(symbol, number, letter)
    elif letter + number + symbol < 15:
        print('\tYeah STRONG.')
        condition(symbol, number, letter)
    else:
        print('\tRELAX, YOU ARE SAFE.')
        condition(symbol, number, letter)
else:
    print('FAILED...Your Password ain\'t Valid')
    condition(symbol, number, letter)

