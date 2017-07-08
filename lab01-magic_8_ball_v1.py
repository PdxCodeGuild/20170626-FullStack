
# lab 1: magic 8-ball
# declare a list of phrases
# ask the user a question (which we do nothing with)
# then pick a random response

import random

phrases = ['It is certain', 'Most likely', 'Signs point to yes', 'Reply hazy try again', 'Concentrate and ask again', 'Better not tell you now']
question = input('what is your question? ')
random_index = random.randint(0, len(phrases)-1)
random_answer = phrases[random_index]
print(random_answer)

