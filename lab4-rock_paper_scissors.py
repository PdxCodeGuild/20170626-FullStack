
# lab 4: play rock-paper-scissors with the computer
# 1) we get the user's choice
# 2) we check to make sure that what the user entered was among the valid possibilities
# 3) the computer randomly picks rock, paper, or scissors
# 4) depending on the choices, the program declares a winner or a tie

# below are the various combinations:
# rock - rock
# rock - scissors
# rock - paper
# scissors - rock
# scissors - scissors
# scissors - paper
# paper - rock
# paper - scissors
# paper - paper

import random

rps = ['rock', 'paper', 'scissors']
user_choice = input('which do you choose: rock, paper, or scissors? ')
print('user chooses: '+user_choice)
if user_choice in rps:
	random_index = random.randint(0, 2) #get a random index: 0, 1, or 2
	comp_choice = rps[random_index] #get a random choice of 'rock', 'paper' or 'scissors
	print('computer chooses: '+comp_choice)
	if user_choice == comp_choice: #we can eliminate 3 possibilities with one if
		print('tie!')
	elif user_choice == 'rock' and comp_choice == 'scissors':
		print('user wins!')
	elif user_choice == 'rock' and comp_choice == 'paper':
		print('computer wins!')
	elif user_choice == 'scissors' and comp_choice == 'rock':
		print('computer wins!')
	elif user_choice == 'scissors' and comp_choice == 'paper':
		print('user wins!')
	elif user_choice == 'paper' and comp_choice == 'rock':
		print('user wins!')
	elif user_choice == 'paper' and comp_choice == 'scissors':
		print('computer wins!')
else:
	print('you entered an invalid string')



