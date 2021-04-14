from tkinter import *
from datetime import datetime

window=Tk()
window.title("SafeStore - Passwords")
window.geometry("450x450")
window.resizable(0,0)

# iniatialize frames
f_login=Frame(window)
f_check=Frame(window)
# f_fail=Frame(window)
f_new=Frame(window)

for frame in (f_login,f_check,f_new):
    frame.grid(row=0,column=0,sticky='nsew')

# define show_frame

def show_frame(frame):
    frame.tkraise()

# converting the password, to leakProof encoding (lol)

def encode_pswd(og_pswd,add):
    encode='AabBcC1d!DEefFG2gHh@I#i3j4k5JKl6L$mM7noN%8OPpQqr9RSs0TUtuV&vwWX*xyYzZ'
    custom_hash=''
    for letter in og_pswd:
        print(letter)
        for i in range(len(encode)):
            if letter==encode[i]:
                find_loc=i
        print(find_loc)
        change=int(find_loc)+int(add)
        print(change)
        if change<69:
            custom_hash+=encode[change]
            print('BOOOOOOMMMMMMMM - ', custom_hash)
        else:
            change=change-69
            custom_hash+=encode[change]
            print('BOOOOOOMMMMMMMM 2222222222222 - ', custom_hash)
    print(custom_hash)

#==================Frame SIGN-IN code

def check_login():
    show_frame(f_check)
    if inp_usrn.get()=='' and inp_pswd.get()=='':
        back=Button(f_check, text="<--",font=('bold',10),width=10,command=lambda:show_frame(f_login))
        back.grid(row=0,column=0,sticky='nsew')

        login_succ=Label(f_check,text="Sign-In Successful.",width=30,font=("bold",14))
        login_succ.grid(row=0,column=1,sticky='w')

        clickOK=Button(f_check, text="OK.",font=('bold',10),width=18,command=lambda:show_frame(f_new))
        clickOK.grid(row=1,column=1,sticky='nsew')

    else:
        login_fail=Label(f_check,text="Sign-In Failed.",width=30,font=("bold",14))
        login_fail.grid(row=0,column=1,sticky='w')

        clickOK=Button(f_check, text="OK.",font=('bold',10),width=18,command=lambda:show_frame(f_login))
        clickOK.grid(row=1,column=1,sticky='nsew')

#==================Frame LogIn code

label_title=Label(f_login,text="SafeStore - Passwords",width=30,font=("bold",14,"underline"))
label_title.grid(row=0,columnspan=4,sticky='w')

label_usrn=Label(f_login,text="UserName - ",width=10,font=("bold",14))
label_usrn.grid(row=1,column=1,sticky='w')

inp_usrn=Entry(f_login,width=18)
inp_usrn.grid(row=1,column=2,ipadx=10,ipady=5)

label_pswd=Label(f_login,text="Password - ",width=10,font=("bold",14))
label_pswd.grid(row=2,column=1,sticky='w')

inp_pswd=Entry(f_login,width=18)
inp_pswd.grid(row=2,column=2,ipadx=10,ipady=5)

# if len(inp_usrn.get())>0 and len(inp_pswd.get())>0:
#     print('InHEre? when')
#     signin.config(state=ACTIVE)

signin=Button(f_login,text="SIGN-IN",font=('bold',10),width=18,command=check_login)
signin.grid(row=3,column=1,sticky='nsew')

# signup=Button(f_login,text="SIGN-UP",font=('bold',10),width=18,command=lambda:show_frame(f_new))
# signup.grid(row=3,column=2,sticky='nsew')

quit=Button(f_login,text="EXIT.",font=('bold',10),width=18,command=window.destroy)
quit.grid(row=4,column=2,sticky='nsew')

#==================Frame SIGN-UP code


#==================Frame NEW Detail Store code

back=Button(f_new, text="<--",font=('bold',10),width=7,command=lambda:show_frame(f_login))
back.grid(row=0,column=0,sticky='nsew')

label_title_newpg=Label(f_new,text="Create New Entry",width=30,font=("bold",14,"underline"))
label_title_newpg.grid(row=0,column=1,columnspan=2,sticky='nsew')

time_save=str(datetime.time(datetime.now())).split('.')
label_time=Label(f_new,text=time_save[0],width=7,font=(12))
label_time.grid(row=1,column=0,sticky='w')

enter_webs=Label(f_new,text="Enter Website/FileName - ",width=20,font=('bold',12))
enter_webs.grid(row=2,column=1,sticky='w')

input_webs=Entry(f_new,width=18)
input_webs.grid(row=2,column=2,ipadx=10,ipady=5)

enter_usrn=Label(f_new,text="Enter UserName - ",width=20,font=('bold',12))
enter_usrn.grid(row=3,column=1,sticky='w')

input_usrn=Entry(f_new,width=18)
input_usrn.grid(row=3,column=2,ipadx=10,ipady=5)

enter_pswd=Label(f_new,text="Enter Password - ",width=20,font=('bold',12))
enter_pswd.grid(row=4,column=1,sticky='w')

input_pswd=Entry(f_new,width=18)
input_pswd.grid(row=4,column=2,ipadx=10,ipady=5)

enter_secans=Label(f_new,text="Enter Security Answer - ",width=20,font=('bold',12))
enter_secans.grid(row=5,column=1,sticky='w')

input_secans=Entry(f_new,width=18)
input_secans.grid(row=5,column=2,ipadx=10,ipady=5)

cond_add=str(time_save[0]).split(':')
save=Button(f_new,text="SAVE.",font=('bold',12),width=18,command=lambda: encode_pswd(input_pswd.get(),cond_add[1]))
save.grid(row=6,column=1,columnspan=2,sticky='nsew')

show_frame(f_login)
window.mainloop()
