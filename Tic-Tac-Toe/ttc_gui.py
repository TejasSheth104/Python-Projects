# tic-tac-toe GUI

from tkinter import *

def mode(option):
    if option==1:
        pass
    elif option==2:
        pass

window = Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")

# lab1=Label(window, text="Welcome, ---", width=30,height=4)
# lab1.grid(row=0, columnspan=3, sticky='e')

opt1=Button(window, text="PLAYER vs COMPUTER", command=lambda: mode('1'), width=40,height=1)
opt2=Button(window, text="PLAYER1 vs PLAYER2", command=lambda: mode('2'), width=40,height=1)
opt3=Button(window, text="EXIT", command=window.destroy, width=40,height=1)
opt1.grid(row=1, columnspan=4)
opt2.grid(row=2, columnspan=4)
opt3.grid(row=3, columnspan=4)

grid_but1=Button(window, text=" ", width=15,height=4)
grid_but1.grid(row=4,column=1)
grid_but2=Button(window, text=" ", width=15,height=4)
grid_but2.grid(row=4,column=2)
grid_but3=Button(window, text=" ", width=15,height=4)
grid_but3.grid(row=4,column=3)
grid_but4=Button(window, text=" ", width=15,height=4)
grid_but4.grid(row=5,column=1)
grid_but5=Button(window, text=" ", width=15,height=4)
grid_but5.grid(row=5,column=2)
grid_but6=Button(window, text=" ", width=15,height=4)
grid_but6.grid(row=5,column=3)
grid_but7=Button(window, text=" ", width=15,height=4)
grid_but7.grid(row=6,column=1)
grid_but8=Button(window, text=" ", width=15,height=4)
grid_but8.grid(row=6,column=2)
grid_but9=Button(window, text=" ", width=15,height=4)
grid_but9.grid(row=6,column=3)

# lab_res=Label(window, text="Winner is - ", width=40,height=2)
# lab_res.grid(row=0, columnspan=4, sticky='e')

window.mainloop()
