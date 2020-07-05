# Password Generator
# Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be, and how many letters
# and numbers they want in their password. Have a mix of upper and lowercase letters,
# as well as numbers and symbols. The password should be a minimum of 6 characters long.

# generate a random password ,
# ask for the length, no of letters and no of numbers,
# mix of upper n lower case , and numbers and symbols,
# minimum of 6 characters

import random
alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
numsym = '1234567890@._-#$%*!'
get_pass = list()
generate = list()
length, chars, num_sym, password = 0, 0, 0, ""

# while True:
try:
    length = int(input('Enter Length of your Desired Password - '))
    if length < 6 or length > 20:
        print('Out of Bounds Error')
        exit(404)
    chars = int(input('Enter Count of Letters in your Desired Password - '))
    num_sym = length - chars
except ValueError:
    print('InValid Input.')
    exit(-1)
count = 1
while count <= chars:
    print(count, chars)
    get_pass.append(random.choice(alphas))
    count += 1
count = 1
while count <= num_sym:
    print(count, num_sym)
    get_pass.append(random.choice(numsym))
    count += 1

print(get_pass)
for temp in range(length):
    generate.append(random.choice(get_pass))
print(generate)
for mix in generate:
    password = password + str(mix)

print('Your Password is - ', password)
