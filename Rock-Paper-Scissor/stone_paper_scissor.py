# rock, paper, scissor, player v computer
# computers ans will be random and shld prompt user for their input
# while and if statements understanding
# 2 end

# 2nd mini project

import random


player1 = 0
player_computer = 0
user = ''
update = 0
collection = ['rock', 'paper', 'scissor']
print('5-Point Game: - \n')
print('1. Rock')
print('2. Paper')
print('3. Scissor')
print('Enter Corresponding Numeric Values: ')
while (player_computer < 5) and (player1 < 5):
    try:
        user = int(input('Your Move: '))
        if (user >= 1) and (user <= 3):
            update = user - 1
    except:
        print('Invalid Option Entered. ')
        print('Game Ended Abruptly')
        exit(0)

    comp = random.choice(collection)
    syst = collection.index(comp)
    gamer = collection[update]
    print("\nUser's Move:", gamer)
    print("Computer's Move:", comp)

    if syst + 1 == 1 and user == 3:
        player_computer += 1
    elif syst + 1 == 2 and user == 1:
        player_computer += 1
    elif syst + 1 == 3 and user == 2:
        player_computer += 1
    elif user == 1 and syst + 1 == 3:
        player1 += 1
    elif user == 2 and syst + 1 == 1:
        player1 += 1
    elif user == 3 and syst + 1 == 2:
        player1 += 1
    print('Score: \nPlayer: {} \'vs\' Computer: {}\n'.format(player1, player_computer))

print('Final Score: \nPlayer: {} \'vs\' Computer: {}'.format(player1, player_computer))
