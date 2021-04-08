# tic-tac-toe GUI

from tkinter import *
from tkinter.messagebox import *
from itertools import permutations

window=Tk()
p_val=""
counter=0
terminate=False
player1,player2=list(),list()
keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

def draw_grid(window,button_play1,button_play2):
# 9 variables to set Button Value later (X/O)
    place_value1, place_value2, place_value3=StringVar(), StringVar(), StringVar()
    place_value4, place_value5, place_value6=StringVar(), StringVar(), StringVar()
    place_value7, place_value8, place_value9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(window, textvariable=place_value1, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(1,place_value1,button_play1,button_play2))
    grid_but1.grid(row=5,column=1)
    grid_but2=Button(window, textvariable=place_value2, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(2,place_value2,button_play1,button_play2))
    grid_but2.grid(row=5,column=2)
    grid_but3=Button(window, textvariable=place_value3, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(3,place_value3,button_play1,button_play2))
    grid_but3.grid(row=5,column=3)
    grid_but4=Button(window, textvariable=place_value4, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(4,place_value4,button_play1,button_play2))
    grid_but4.grid(row=6,column=1)
    grid_but5=Button(window, textvariable=place_value5, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(5,place_value5,button_play1,button_play2))
    grid_but5.grid(row=6,column=2)
    grid_but6=Button(window, textvariable=place_value6, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(6,place_value6,button_play1,button_play2))
    grid_but6.grid(row=6,column=3)
    grid_but7=Button(window, textvariable=place_value7, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(7,place_value7,button_play1,button_play2))
    grid_but7.grid(row=7,column=1)
    grid_but8=Button(window, textvariable=place_value8, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(8,place_value8,button_play1,button_play2))
    grid_but8.grid(row=7,column=2)
    grid_but9=Button(window, textvariable=place_value9, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press(9,place_value9,button_play1,button_play2))
    grid_but9.grid(row=7,column=3)

def win_cond():
# generates every Winning Possibility using inbuilt Permutation Function.
    global counter,terminate,player1,player2
    poss_1=permutations([1,2,3])
    poss_2=permutations([4,5,6])
    poss_3=permutations([7,8,9])
    poss_4=permutations([1,4,7])
    poss_5=permutations([2,5,8])
    poss_6=permutations([3,6,9])
    poss_7=permutations([1,5,9])
    poss_8=permutations([3,5,7])
    
# check if ANY player has matched with the winning condition.
    for i in poss_1,poss_2,poss_3,poss_4,poss_5,poss_6,poss_7,poss_8:
        for j in list(i):
            play1=all(poss in player1 for poss in j)
            play2=all(poss in player2 for poss in j)

            if play1:
                showinfo("RESULT - ","Player 1 WINS. !!!")
                terminate=True
                return terminate
            elif play2:
                showinfo("RESULT - ","Player 2 WINS. !!!")
                terminate=True
                return terminate
            # temp_var=0
            # for value in keypress_count.values():
            #     if value==1:
            #         temp_var=1
            #     else:
            #         temp_var=0
            #         break
            # if temp_var==1:
            #     showinfo("RESULT - ","It's a DRAW. !!!")
            #     terminate=True
            #     return terminate

def chance(box_num,button_play1,button_play2):
# iterate over 1 to 9, to Toggle Button and Check for Players Chance
    global counter,player1,player2
    for box_num_value in range(1,10):
        if box_num==box_num_value:
            if counter%2==0:
                counter+=1
                button_play1.config(state=DISABLED)         # disable button 1
                button_play2.config(state=ACTIVE)           # enable button 2
                player1.append(box_num)
                return 'X'
            else:
                counter+=1
                button_play2.config(state=DISABLED)         # disable button 2
                button_play1.config(state=ACTIVE)           # enable button 1
                player2.append(box_num)
                return 'O'

# to avoid user from manipulating the values once clicked on the button.
def limit_keypress(box_key):
# if the respective value of dictionary is 0, then its changed to 1 & hence cant be used again.
    global keypress_count
    if keypress_count[box_key]==0:
        keypress_count[box_key]=1
        return True
    else:
        return False

def key_press(box_num,place_value,button_play1,button_play2):
# if value of dictionary is 1 already(returning Value FALSE.), no change takes place.
    global p_val,counter,window,terminate,keypress_count,player1,player2
    if limit_keypress(box_num):
        p_val=chance(box_num,button_play1,button_play2)
        place_value.set(p_val)
# sets the value (X/O) at respective position.
        if win_cond():
            msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")
# reset every parameter, and call the Grid Function to restart.
            if msg=='yes':
                terminate=False
                counter=0
                p_val=""
                player1,player2=list(),list()
                keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
                draw_grid(window)
# thank you message and exit.
            if msg=='no':
                showinfo("EXIT","THANK YOU. !!!")
                window.destroy()

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("340x400")

# Highlighted Button, implies that players turn to play.
    button_play1=Button(window, text="Player1: 'X'", font=('arial',10,'bold') ,width=18,height=1)
    button_play1.grid(row=1, columnspan=4,sticky='w')

    button_play2=Button(window, text="Player2: 'O'", font=('arial',10,'bold') ,width=18,height=1,state=DISABLED)
    button_play2.grid(row=1, columnspan=4,sticky='e')

# a 3x3 grid to play on.
# passing button1 and button2 as parameters to help toggle at every chance.
    draw_grid(window,button_play1,button_play2)

    reset_button=Button(window, bg='black', fg='red', text="RESET", command=main_body, font=('arial',10,'bold') ,width=18,height=1)
    reset_button.grid(row=8,columnspan=4,sticky='w')
# exit button to terminate program immediately
    quit_button=Button(window, bg='black', fg='red', text="EXIT", command=window.destroy, font=('arial',10,'bold') ,width=18,height=1)
    quit_button.grid(row=8,columnspan=4,sticky='e')

    window.mainloop()

if __name__ == '__main__':
    main_body()
