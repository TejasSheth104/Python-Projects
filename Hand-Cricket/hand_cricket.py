# hand cricket...
# 3 end
# 3rd Mini-Project

# Hangman
# This is probably the hardest one out of these 6 small projects.
# This will be similar to guessing the number, except we are guessing the word.
# The user needs to guess letters,
# Give the user no more than 6 attempts for guessing wrong letter.
# This will mean you will have to have a counter.
# You can download a ‘sowpods’ dictionary file or
# csv file to use as a way to get a random word to use.
import random
import os


def player_bat(*fetch_required):
    fetch = int(fetch_required[0])
    counts = ['0', '1', '2', '3', '4', '5', '6']
    wicket = 0
    balls = 0
    player_score = 0
    while wicket < 1 and balls < 10 and player_score < fetch:
        computer_select = int(random.choice(counts))
        balls += 1
        print('Ball No.:', balls)
        try:
            user_select = int(input('enter value(0 to 6): '))
        except:
            print('Un-Excepted Value Encountered...\nRetry Again...')
            continue
        if user_select < 0 or user_select > 6:
            print('Value out of Range')
            break
        print('Player:', user_select, '\nComputer:', computer_select)
        if user_select == computer_select:
            print('WICKET ---> PLAYER OUT....')
            wicket += 1
            print('Player\'s Score = ', player_score, '\nWickets = ', wicket)
    #                for i in range(10000*10000):
    #                    continue
    #                clear()
        else:
            player_score += user_select
            print('Player\'s Score = ', player_score, '\n')
    #                for i in range(10000*10000):
    #                    continue
    #                clear()
#    print(player_score, wicket, balls)
    return player_score, wicket, balls


def computer_bat(*fetch_required):
    fetch = int(fetch_required[0])
    computer_score = 0
    counts = ['0', '1', '2', '3', '4', '5', '6']
    wicket = 0
    balls = 0
    while wicket < 1 and balls < 10 and computer_score < fetch:
        computer_select = int(random.choice(counts))
        balls += 1
        print('Ball No.:', balls)
        try:
            user_select = int(input('enter value(0 to 6): '))
        except:
            print('Un-Excepted Value Encountered...\nRetry Again...')
            continue
        if user_select < 0 or user_select > 6:
            print('Value out of Range')
            break
        print('Player:', user_select, '\nComputer:', computer_select)
        if user_select == computer_select:
            print('WICKET - PLAYER OUT....')
            wicket += 1
            print('Computer\'s Score = ', computer_score, '\nWickets = ', wicket)
        #                for i in range(10000*10000):
        #                  continue
        #                clear()
        else:
            computer_score += computer_select
            print('Computer\'s Score = ', computer_score, '\n')
    #                for i in range(10000*10000):
    #                    continue
    #                clear()
#    print(computer_score, wicket, balls)
    return computer_score, wicket, balls


def game(toss_winner, selected, *chase):
    follow = int(chase[0])
#    print(follow, '\n')
    if ((toss_winner.lower() == 'player') and (selected.lower() == 'bat')) or \
            ((toss_winner.lower() == 'computer') and (selected.lower() == 'bowl')):
        player_score, wicket, balls = player_bat(follow)
        return player_score, wicket, balls
    elif ((toss_winner.lower() == 'player') and (selected.lower() == 'bowl')) or \
            ((toss_winner.lower() == 'computer') and (selected.lower() == 'bat')):
        computer_score, wicket, balls = computer_bat(follow)
        return computer_score, wicket, balls


clear = lambda: os.system('cls')
select = ['Bat', 'Bowl']
toss = ['Heads', 'Tails']
choice = random.choice(toss)
target = 1000000
p_score = 0
c_score = 0
outs_player = 0
outs_computer = 0
computer_balls_faced = 0
player_balls_faced = 0
print('Toss Time: Heads / Tails')
call = str(input('Player Calls: '))
if call.upper() == choice.upper():
    print('Player WON the Toss')
    choose = str(input('BAT or BOWL: '))
    if choose.lower() == 'bat':
        p_score, outs_player, player_balls_faced = game('Player', choose, target)
        target = p_score + 1
        print('\nTarget is:', target, '\n')
        c_score, outs_computer, computer_balls_faced = game('Computer', choose, target)
    elif choose.lower() == 'bowl':
        c_score, outs_player, computer_balls_faced = game('Player', choose, target)
        target = c_score + 1
        print('\nTarget is:', target, '\n')
        p_score, outs_computer, player_balls_faced = game('Computer', choose, target)
else:
    print('Computer WON the Toss')
    choose = random.choice(select)
    print('Choose to: ', choose)
    if choose.lower() == 'bat':
        c_score, outs_computer, computer_balls_faced = game('Computer', choose, target)
        target = c_score + 1
        print('\nTarget is:', target, '\n')
        p_score, outs_player, player_balls_faced = game('Player', choose, target)
    elif choose.lower() == 'bowl':
        p_score, outs_computer, player_balls_faced = game('Computer', choose, target)
        target = p_score + 1
        print('\nTarget is:', target, '\n')
        c_score, outs_player, computer_balls_faced = game('Player', choose, target)

print('\n')
if p_score < c_score:
    print('Computer - {}/{} __vs__ Player - {}/{}'.format(c_score, outs_computer, p_score, outs_player))
    print('\tWINNER - Computer.')
elif c_score < p_score:
    print('Player - {}/{} __vs__ Computer - {}/{}'.format(p_score, outs_player, c_score, outs_computer))
    print('\tWINNER - Player.')
elif p_score == c_score:
    print('IT\'S A DRAW...\nWINNER ON BASIS OF WICKET\'S LOST...')
    if outs_player < outs_computer:
        print('Player - {}/{} __vs__ Computer - {}/{}'.format(p_score, outs_player, c_score, outs_computer))
        print('\tWINNER - Player.')
    elif outs_player > outs_computer:
        print('Computer - {}/{} __vs__ Player - {}/{}'.format(c_score, outs_computer, p_score, outs_player))
        print('\tWINNER - Computer.')
    elif outs_computer == outs_player:
        print('IT\'S A DRAW AGAIN...\nWINNER ON BASIS OF BALL\'S FACED...')
        if player_balls_faced > computer_balls_faced:
            print('Computer - {}/{} __vs__ Player - {}/{}'.format(c_score, outs_computer, p_score, outs_player))
            print('\tWINNER - Computer.')
        elif player_balls_faced < computer_balls_faced:
            print('Player - {}/{} __vs__ Computer - {}/{}'.format(p_score, outs_player, c_score, outs_computer))
            print('\tWINNER - Player.')
else:
    print('IT\'S A RARE DRAW ...')
    print('Player - {}/{} __vs__ Computer - {}/{}'.format(p_score, outs_player, c_score, outs_computer))
    print('\tWINNER - CODE DEVELOPER.')
