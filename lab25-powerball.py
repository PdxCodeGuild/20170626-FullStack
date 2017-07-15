
# lab 25: play powerball many times, determine net balance

# initially the program will pick 6 random numbers as the 'winner'
# then will buy tickets to play 100,000 times
# the price of a ticket is $2
# a ticket contains 6 numbers, 1 to 99
# calculate your net winnings

# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win #1,000,000
# if 6 numbers match, you win #25,000,000

import random

def pick6():
    return [random.randint(1,99) for i in range(6)]

def check_ticket(ticket, winners):
    
    # count how many numbers match

    # non-pythonic way
    # n_match = 0
    # for i in range(len(ticket)):
    #     if ticket[i] == winners[i]:
    #         n_match += 1

    # pythonic way
    n_match = sum(a == b for a,b in zip(ticket, winners))

    prizes = [0,7,100,50000,1000000,25000000]
    return prizes[n_match]


n_tries = 100000
winners = pick6()


# v1, just calculate net balance
# balance = 0
# for i in range(n_tries):
#     balance -= 2
#     ticket = pick6()
#     balance += check_ticket(ticket, winners)
# print('final balance: ' + str(money))


# v2, calculate return on investment
earnings = 0
for i in range(n_tries):
    ticket = pick6()
    earnings += check_ticket(ticket, winners)
expenses = 2*n_tries
net = earnings - expenses
roi = (earnings - expenses)/expenses
print('earnings: ' + str(earnings))
print('expenses: ' + str(expenses))
print('net: ' + str(net))
print('return on investment: ' + str(roi))
