
# lab 2: check if the user's string is a palindrome (e.g. 'racecar')
# we first compare the first and last letters
# then we compare the second and the second-to-last letters
# and so on, comparing each half to the other half
# if any of our checks fail, return false
# if all our tests succeed, return true

def check_palindrome(string):
    half_len = len(string) // 2 #we only need to loop through half the string
    for i in range(half_len):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

user_input = input('what is your word? ') #get the word from the user
print(check_palindrome(user_input)) #show the user the result of check_palindrome
