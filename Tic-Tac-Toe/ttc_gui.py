# tic-tac-toe GUI

from tkinter import *
import random

p_val=""

def draw_grid(window):
    place_value1, place_value2, place_value3=StringVar(), StringVar(), StringVar()
    place_value4, place_value5, place_value6=StringVar(), StringVar(), StringVar()
    place_value7, place_value8, place_value9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(window, textvariable=place_value1, width=10,height=4, command=lambda: key_press("",place_value1))
    grid_but1.grid(row=5,column=1)
    grid_but2=Button(window, textvariable=place_value2, width=10,height=4, command=lambda: key_press("",place_value2))
    grid_but2.grid(row=5,column=2)
    grid_but3=Button(window, textvariable=place_value3, width=10,height=4, command=lambda: key_press("",place_value3))
    grid_but3.grid(row=5,column=3)
    grid_but4=Button(window, textvariable=place_value4, width=10,height=4, command=lambda: key_press("",place_value4))
    grid_but4.grid(row=6,column=1)
    grid_but5=Button(window, textvariable=place_value5, width=10,height=4, command=lambda: key_press("",place_value5))
    grid_but5.grid(row=6,column=2)
    grid_but6=Button(window, textvariable=place_value6, width=10,height=4, command=lambda: key_press("",place_value6))
    grid_but6.grid(row=6,column=3)
    grid_but7=Button(window, textvariable=place_value7, width=10,height=4, command=lambda: key_press("",place_value7))
    grid_but7.grid(row=7,column=1)
    grid_but8=Button(window, textvariable=place_value8, width=10,height=4, command=lambda: key_press("",place_value8))
    grid_but8.grid(row=7,column=2)
    grid_but9=Button(window, textvariable=place_value9, width=10,height=4, command=lambda: key_press("",place_value9))
    grid_but9.grid(row=7,column=3)

def play_uservcomp(window):
    draw_grid(window)
    pass

def play_uservuser(window):
    draw_grid(window)
    pass

def chance():
    opt=('X', 'O')
    return random.choice(opt)

def key_press(val,place_value):
    global p_val
    p_val=chance()+val
    place_value.set(p_val)
    

# def mode(option):
#     if option==1:
#         play_uservcomp()
#     elif option==2:
#         play_uservuser()

def main_body():
    window = Tk()
    window.title("Tic Tac Toe")
    window.geometry("300x400")

    # lab1=Label(window, text="Welcome, ---", width=30,height=4)
    # lab1.grid(row=0, columnspan=3, sticky='e')

    # opt1=Button(window, text="PLAYER vs COMPUTER", command=lambda: mode('1'), width=30,height=1)
    # opt2=Button(window, text="PLAYER1 vs PLAYER2", command=lambda: mode('2'), width=30,height=1)
    opt1=Button(window, text="PLAYER vs COMPUTER (click again to RESET)", command=lambda: play_uservcomp(window), width=35,height=1)
    opt2=Button(window, text="PLAYER1 vs PLAYER2 (click again to RESET)", command=lambda: play_uservuser(window), width=35,height=1)
    opt3=Button(window, text="EXIT", command=window.destroy, width=30,height=1)
    opt1.grid(row=0, columnspan=4)
    opt2.grid(row=1, columnspan=4)
    opt3.grid(row=2, columnspan=4)

    lab_res=Label(window, text="Winner is - ", width=40,height=2)
    lab_res.grid(row=4, columnspan=4)

    window.mainloop()

if __name__ == '__main__':
    main_body()
