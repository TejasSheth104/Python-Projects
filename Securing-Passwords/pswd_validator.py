# enter your password to verify its strength
# check of Capital letters, Symbols, Numbers
#
import string
letters = string.ascii_letters
numbers = string.digits
symbols = "\\!@#$%^&*()_-;|:,.><?/"


def condition(count_symbols, count_number, count_letter, pswd):
    if count_symbols < 1: print('Use More Special Characters.')
    if count_number <= (int(len(pswd) / 3)): print('Use More Numerical Characters.')
    if count_letter <= (int(len(pswd) / 3)): print('Use More Letters.')


def validator():
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
            condition(symbol, number, letter, pswd)
        elif letter + number + symbol < 15:
            print('\tYeah STRONG.')
            condition(symbol, number, letter, pswd)
        else:
            print('\tRELAX, YOU ARE SAFE.')
            condition(symbol, number, letter, pswd)
    else:
        print('FAILED...Your Password ain\'t Valid')
        condition(symbol, number, letter, pswd)

