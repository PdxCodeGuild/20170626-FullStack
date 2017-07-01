
# lab 6: generate a password containing a random string of letters
# 1) get the length of the password from the user
# 2) loop the same number of times as the length of the password
# 3) for each iteration, pick a random character from char_set, and append it to a running password
# 4) print out the generated password

import random

# alternatively use string.ascii_letters and/or string.digits
char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # the string from which we'll randomly pull characters
password_length = int(input('how long will the password be? ')) # get the user input
password = '' # start with an empty string
for i in range(password_length):
    random_char = random.choice(char_set) # get a random character from char_set
    password += random_char # add it to our password
print(password)

