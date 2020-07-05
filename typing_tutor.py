# your personal typing tutor.
# We will be randomly selecting a given number of words from this list
# For score calculation, we increment score by one each time a letter is correctly pressed by user. 
# Also a time limit is assigned to each word, which is a multiple of the word length. 
# If the user types the word before the time limit, the leftover time gets added to the score.

import random

# clearing the smaller words from the file 'engmix.txt'
word_list = list()
filehandle = open('engmix.txt')
for word in filehandle:
    print(word, end=" ")
    # if len(word) > 3:
    #     word_list.append(word)
    
# print(word_list)