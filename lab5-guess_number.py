
# lab 5: the computer randomly picks a value, the user has to guess

# v1: the user is told they're incorrect, and given another chance to guess
# v2: the user is told whether the target is higher or lower than the guess
# v3: the user is told whether their latest guess is closer or further from the target than their last guess

import random

def abs_distance(a, b):
	return abs(a-b)

target = random.randint(1, 10) #pick a random number: 1,2,3...10
last_guess = -1
while True:
	guess = int(input('guess a number: '))
	if guess == target:
		print('correct!')
		break
	#else:
	#	print('incorrect!')
	
	#v2
	#if target > guess:
	#	print('higher!')
	#else:
	#	print('lower!')
	
	#v3
	if last_guess != -1:
		d_last_guess = abs_distance(last_guess, target)
		d_guess = abs_distance(guess, target)
		if d_guess < d_last_guess:
			print('closer!')
		elif d_guess > d_last_guess:
			print('further!')
		else:
			print('you\'re the same distance away')
	
	last_guess = guess #set the value up for the next iteration
	


