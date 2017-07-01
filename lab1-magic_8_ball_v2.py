
# lab 1: magic 8-ball
# collect a list of possible phrases from the user
#   e.g. 'yes', 'no', 'certainly' etc
# then ask the user a question
#   e.g. 'will I meet the love of my life tomorrow?'
# the program then chooses a random phrase from those entered and prints it

import random

phrases = [] #initialize phrases as an empty list
while True: # this will loop forever, unless we 'break'
    current_phrase = input('What is the next value? (type "done" if done) \n')
    if current_phrase == 'done':
        break # if the user enters 'done', exit the loop
    else:
        phrases.append(current_phrase) # add the phrase entered by the user to the list

question = input('what is your question? ') # get the user's question
random_index = random.randint(0, len(phrases)-1)
random_answer = phrases[random_index]
print(random_answer)


