# from crypto.cipher import AES
# import base64

# msg_text="Hello"

# cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
# encoded = base64.b64encode(cipher.encrypt(msg_text))
# # ...
# decoded = cipher.decrypt(baes64.b64decode(msg_text))

# import hashlib

# s='she sells sea shells by the sea shore'
# s1='tejas1004'
# hashed=hashlib.sha1(s.encode("utf-8")).hexdigest()
# hashed1=hashlib.sha1(s1.encode("utf-8")).hexdigest()
# print(hashed)                                           # adf112cb818ce5a284d049ab580f622363de5cce
# print(hashed1)                                          # 2b958566bd14a904bdf83f7007043d00a5696f07

'''

1. take input username password
2. generate a hashed value for the password -
        
        a. instead of inbuild hash function, create a ever changing 
            Custom Designed encoding system that changes itself periodically,
        b. can even recreate the password, if we know the given conditions for it.

3. save the username password hashed value in DB
4. when requested for the desired password, first show username and hashed value
5. ask for a authentication key, and only then show the real password.

6. try to save all this data in a file/db/anywhere.
7. make a GUI interface
8. create an EXE file to use on the go.

'''
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_-
# eg inp= Tejas1004 ; custHash= (date=3) Whmdv4##7
# store in DB, (date/any parameter that will be used) | (username=OG/madeup) | (password=madeup)

from datetime import datetime

inp_username=input('Enter Username - ')
inp_password=input('Enter Passowrd - ')

custom_hash,og_pswd='',''
encode='AabBcC1d!DEefFG2gHh@I#i3j4k5JKl6L$mM7noN%8OPpQqr9RSs0TUtuV&vwWX*xyYzZ'

def generate_og_pwsd(hashed):
    for letter in hashed:
        for i in range(len(encode)):
            if letter==encode[i]:
                find_loc=i
    change_back=int(find_loc)-int(condition[i])
    if change_back<=0:
        og_pswd+=encode[-change_back]
        print('BOOOOOOMMMMMMMM - ', og_pswd)
    else:
        change_back=change_back+69
        og_pswd+=encode[-change_back]
        print('BOOOOOOMMMMMMMM 2222222222222 - ', og_pswd)
print(og_pswd)


condition=str(datetime.time(datetime.now())).split(':')
print(condition)
for letter in inp_password:
    print(letter)
    for i in range(len(encode)):
        if letter==encode[i]:
            find_loc=i
    print(find_loc)
    change=int(find_loc)+int(condition[1])
    print(change)
    if change<69:
        custom_hash+=encode[change]
        print('BOOOOOOMMMMMMMM - ', custom_hash)
    else:
        change=change-69
        custom_hash+=encode[change]
        print('BOOOOOOMMMMMMMM 2222222222222 - ', custom_hash)
print(custom_hash)
generate_og_pwsd(custom_hash)





