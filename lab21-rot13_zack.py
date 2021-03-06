
# lab 21: rot 13, Zack's solution using a dictionary comprehension

import string

def dynamic_rot_encode(_string, n):
    cipher = {chr(97 + ((i + n) % 26)) : chr(97 + i) for i in range(26)}
    cipher.update({chr(65 + ((i + n) % 26)) : chr(65 + i) for i in range(26)})
    
    return ''.join([cipher[char]
                    if char not in string.punctuation and not char.isspace()
                    and not char.isdigit()
                    else char
                    for char in _string])

def dynamic_rot_decode(_string, n):
    return dynamic_rot_encode(_string, -n)

encoded_string = dynamic_rot_encode('Hello 7 worlds and stuff?!', 13)

print(encoded_string)
print(dynamic_rot_decode(encoded_string, 13))