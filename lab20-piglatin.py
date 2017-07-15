
# lab 20: piglatin

# If the first letter is a consonant, move it to the end
# Add "ay" to the end of that
# If the first letter is a vowel, just add "yay" to the end

vowels = 'aeiou'
word = input('what is your word? ')
if len(word) > 1:
    if word[0] in vowels:
        word += 'yay'
    else:
        word = word[1:] + word[0] + 'ay'
print(word)
