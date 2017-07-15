
# lab 18: roll m n-sided die

from random import randint

n_dice = int(input('how many dice would you like to throw? '))
n_sides = int(input('how many sides do the dice have? '))

for i in range(n_dice):
    dice_value = randint(1, n_sides)
    print('roll ' + str(i+1) + ': ' + str(dice_value))


