# tic-tac-toe GUI

from tkinter import *
import tic_tac_toe as ttc

window = Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")

lab1=Label(window, text="Welcome, ---", height=10, width=50)
lab1.grid(row=0, columnspan=3, sticky='e')

def mode(option):
    if option==1:
        pass
    elif option==2:
        pass
    elif option==3:
        pass

opt1=Button(window, text="Option 1", command=lambda: mode('1')).grid(row=1, column=0)
opt2=Button(window, text="Option 2", command=lambda: mode('2')).grid(row=1, column=1)
opt3=Button(window, text="Option 3", command=lambda: mode('3')).grid(row=1, column=2)


window.mainloop()
