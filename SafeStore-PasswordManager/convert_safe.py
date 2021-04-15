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

def decode_pswd():
    pass
