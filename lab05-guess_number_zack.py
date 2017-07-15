
# lab 5: the computer randomly picks a value, the user has to guess

import random

random_number = random.randint(0, 10)
old_guess = None # a name without a value

while True:
    current_guess = input('Guess a number: ').strip()
    current_guess = int(current_guess)

    if current_guess == random_number:
        print('You are correct!')
        break

    if old_guess: #a demonstration of 'truthiness'
        old_guess_distance = abs(random_number - old_guess)
        new_guess_distance = abs(random_number - current_guess)

        if old_guess_distance > new_guess_distance:
            print("You are getting warmer")
        if old_guess_distance < new_guess_distance:
            print("You are getting colder")
        elif old_guess_distance == new_guess_distance:
            print("You are not warmer, or colder - really...")

    old_guess = current_guess
