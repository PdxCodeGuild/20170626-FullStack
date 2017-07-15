
# lab 21: rot 13 encoding
# this solution is the more general rot N encoding

# alternative solutions
# use a dirctionary to match one character to another
# use a second encoded alphabet 'nopqrstuvwxyzabcdefghijklm' and match the indices

alphabet = 'abcdefghijklmnopqrstuvwxyz'

user_str = input('what would you like to encode? ')
rot_n = int(input('how far would you like to rotate it? '))

encoded_str = ''
for char in user_str:

    if char not in alphabet: # if the character's not in our alphabet
        encoded_str += char # just add it to the output
        continue # and go to the next character

    index = alphabet.index(char) # get the index for this char
    index_encoded = (index + rot_n)%len(alphabet) # find the index of the encoded character
    encoded_str += alphabet[index_encoded] # add that encoded character to our output

print(encoded_str)








