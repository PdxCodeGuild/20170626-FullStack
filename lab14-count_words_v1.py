
# lab 14 v1: count words
# take a sentence of text
# remove all punctuation, except that which is contained within a word
# e.g. preserve "they're"

# 1) remove punctuation
# 2) make lowercase
# 3) split into words

import string

sentence = 'Python is \'great\', especially for parsing text!'
# result is a list of words: ['python', 'is', 'great', ...]

sentence = sentence.lower()
word_list = sentence.split(' ')
for i in range(len(word_list)):
    word_list[i] = word_list[i].strip(string.punctuation)
print(word_list)




