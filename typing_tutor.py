# your personal typing tutor.
# We will be randomly selecting a given number of words from this list
# For score calculation, we increment score by one each time a letter is correctly pressed by user. 
# Also a time limit is assigned to each word, which is a multiple of the word length. 
# If the user types the word before the time limit, the leftover time gets added to the score.

import random

# clearing the smaller words from the file 'engmix.txt'
word_list = list()
filehandle = open('newwords.txt', errors='ignore')
# fh2 = open('newwords.txt', "a")
# for word in filehandle:
#     if len(word) > 6:
#         print(word, end="")
#         fh2.write(word)
    
# fh2.close()

