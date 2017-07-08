
# lab 16: detect whether two words are anagrams of eachother

# 1) get two words from user
# 2) convert to lowercase
# 3) remove all spaces (replace ' ' with '')
# 4) sort the letters (sorted)
# 5) check if they're equal

def convert_word(word):
    word = word.lower()
    word = word.replace(' ', '')
    word = str(sorted(word))
    return word

#word1 = input('what is the first word? ')
#word2 = input('what is the second word? ')
word1 = 'anagram'
word2 = 'nag a ram'
print('word 1: '+word1)
print('word 2: '+word2)
if convert_word(word1) == convert_word(word2):
    print('those are anagrams!')
else:
    print('those are not anagrams')










