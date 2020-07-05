# Snake and Ladder : uses loop, random
# -> Done. ------- partially
# Typing test : time module, (optional : files, random)
# Stopwatch : time module

import random


# for dice simulation
def dice_roll_sim():
    dice_val = [1, 2, 3, 4, 5, 6]
    return random.choice(dice_val)


# Snake Starting Point Selected Randomly
def snake_mouth(val):
    return random.choices(range(50, 100), k=val)


# Ladder Starting Point Selected Randomly
def ladd_start(val):
    return random.choices(range(1, 50), k=val)


# Snake Ending Point Selected Randomly
def snake_tail(val):
    return random.choices(range(1, 50), k=val)


# Ladder Ending Point Selected Randomly
def ladd_end(val):
    return random.choices(range(50, 100), k=val)


# A Time-Delay Loop to See the Steps going on.
def fordelay(n):
    for _ in range(n*n):
        continue


# main part starts...
num, diff = 0, 0
print('1. Easy\n2. Medium\n3. Hard')
try:
    diff = int(input('Enter Difficulty - '))
    if diff > 3 or diff < 1:
        print('InValid -- ')
        exit(-1)
except TypeError:
    print('Try Again -- ')
    exit(-2)

# setting the difficulties
if diff == 1:
    num, num2 = 5, 10
elif diff == 2:
    num, num2 = 7, 7
else:
    num, num2 = 10, 5

startSnake = snake_mouth(num)
endSnake = snake_tail(num)

startLadd = ladd_start(num2)
endLadd = ladd_end(num2)

snake, ladder = list(), list()
for i in range(len(startSnake)):
    tup = (startSnake[i], endSnake[i])
    snake.append(tup)
for i in range(len(startLadd)):
    tup2 = (startLadd[i], endLadd[i])
    ladder.append(tup2)

position, count, eaten_by_snake, shortcut_using_ladder = 0, 0, 0, 0
print('NOTE - Computer Simulated Game.')
print('Rules - \n1. Get \'1\' to Start\n')
while not position == 100:
    count += 1
    # positioning of Snake and Ladder
    print('Snakes (mouth, tail) - ', sorted(snake))
    print('Ladder (start, end) - ', sorted(ladder))
    print()
    dice = dice_roll_sim()
    print('Position - ', position)
    print('Dice Simulation - ', dice)
    print()
    if position == 0:
        if dice == 1:
            position += dice
            fordelay(5000)
            continue
        else:
            print('Wait Another Round')
            print()
            fordelay(5000)
            continue
    position += dice

    # checking is found a ShortCut Ladder
    for ladder_position in range(len(startLadd)):
        if position == startLadd[ladder_position]:
            shortcut_using_ladder += 1
            print('UHMUHM..! GOT AWAY')
            print(' - - - - - - - - - ')
            position = endLadd[ladder_position]
            fordelay(5000)

    # checking if caught by Snake or not
    for snake_position in range(len(startSnake)):
        if position == startSnake[snake_position]:
            eaten_by_snake += 1
            print('HAHA..! GOT\'ya')
            print(' - - - - - - - ')
            position = endSnake[snake_position]
            fordelay(5000)

    # proceed only if within range, anything excess is skipped.
    while 93 < position < 100:
        count += 1
        dice = dice_roll_sim()
        print('Position Final Third - ', position)
        print('Dice Simulation Final Third - ', dice)
        if dice <= (100 - position):
            position += dice
            fordelay(5000)

    fordelay(5000)


print(' - - - - - - - - - - - - ')
print('WINNER....in - ', count, 'moves')
print('Caught by Snakes - ', eaten_by_snake, 'times')
print('Used ShortCut - ', shortcut_using_ladder, 'times')

# play with users, any number of users.
# currently works with just a single device
# ignores if there is a ladder at the end of snake or a snake at the end of ladder..
