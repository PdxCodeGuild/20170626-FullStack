
# lab 12: mad lib
# collect a series of words from the user
# and put them into a some text

str_adj = input('give me an adjective: ')
str_noun = input('give me a noun: ')
str_animal = input('give me an animal: ')
str_noise = input('give me a noise: ')

print()

output =  str_adj + ' Macdonald had a '+str_noun+', E-I-E-I-O\n'
output += 'and on that '+str_noun+' he had an '+str_animal+', E-I-E-I-O\n'
output += 'with a '+str_noise+' '+str_noise+' here\n'
output += 'and a '+str_noise+' '+str_noise+' there,\n'
output += 'here a '+str_noise+', there a '+str_noise+',\n'
output += 'everywhere a '+str_noise+' '+str_noise+',\n'
output += str_adj+' Macdonald had a '+str_noun+', E-I-E-I-O.'

print(output)
