
# lab 19: blackjack advice

# First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
# Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.
# Lastly, figure out what the playing advice will be. Use the following rules:

# Less than 17, advise to "Hit"
# Over or equal to 17, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Then print out the current total point value and the advice.

cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

card1 = input('what is your first card? ')
card2 = input('what is your second card? ')
card3 = input('what is your third card? ')

total_value = cards[card1] + cards[card2] + cards[card3]
if total_value < 17:
    print(str(total_value) + ': hit!')
elif total_value < 21:
    print(str(total_value) + ': stay!')
elif total_value == 21:
    print(str(total_value) + ': blackjack!')
else:
    print(str(total_value) + ': busted!')

