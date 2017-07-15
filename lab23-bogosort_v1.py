
# lab 23: bogosort using python built-in functions
# keep generating random arrangements of the numbers
# until you happen to find the correct one
# for 10 numbers, there are 10! = 3628800 possible arrangements

from random import randint, shuffle

def bogosort(nums):
    while True:
        shuffle(nums) # randomly shuffle the list
        print(' '.join(nums)) # print out the shuffled sequence
        if sorted(nums) == nums: # check if we've found the sorted list
            return # exit the loop, and the function

nums = [randint(0,99) for i in range(20)] # list comprehension
# nums = [chr(randint(97,97+25)) for i in range(20)] #random letters
print(nums)
bogosort(nums)
print(nums)

