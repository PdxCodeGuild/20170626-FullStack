
# lab 7: count the number of occurances of random numbers between 0 and 9
# e.g. if we only had 4 different numbers and only iterated 5 times
# [0,0,0,0]
# v = 1
# [0,1,0,0]
# v = 3
# [0,1,0,1]
# v = 2
# [0,1,1,1]
# v = 1
# [0,2,1,1]
# v = 1
# [0,3,1,1]

import random

number_counts = [0]*10
for i in range(1000): # loop 1000 times
    v = random.randint(0, len(number_counts)-1) # generate a random value
    number_counts[v] += 1 # increment the count at that index
print(number_counts)
