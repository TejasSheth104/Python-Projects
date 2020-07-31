# write a python program to -
# demonstarte interconversion of different number systems.
# 1.) demical <=> binary
# 2.) demical <=> octal
# 3.) demical <=> hexadecimal
# 4.) octal <=> binary
# 5.) octal <=> hexadecimal
# 6.) hexadecimal <=> binary

from decimal__binary import decimal_binary


while True:
    print('\nSELECT -')
    print('\t0.) Exit')
    print('\t1.) Demical <=> Binary')
    print('\t2.) Demical <=> Octal')
    print('\t3.) Demical <=> Hexadecimal')
    print('\t4.) Octal <=> Binary')
    print('\t5.) Octal <=> Hexadecimal')
    print('\t6.) Hexadecimal <=> Binary')
    try:
        select = int(input('Enter - '))
    except:
        print('Invalid Input.. Try Again.')
        continue
    if 0 > select > 6:
        print('Out of Range.. Try Again')
        continue
    if select == 0:
        print('Thanks.')
        break
    elif select == 1:
        decimal_binary()
    elif select == 2:
        decimal_binary()
    elif select == 3:
        decimal_binary()
    elif select == 4:
        decimal_binary()
    elif select == 5:
        decimal_binary()
    elif select == 6:
        decimal_binary()





