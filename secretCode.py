# Secret Code.

import string
user_input = input('Enter your Message - ')
secretCode = ""
user_input = list(user_input)
for i in range(len(user_input)):
    secretCode += str(ord(user_input[i]))

print(secretCode)

