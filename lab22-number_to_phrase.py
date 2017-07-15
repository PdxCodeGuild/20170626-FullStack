
# lab 22: convert a number between 0 and 99 to a phrase
# e.g. 5 -> 'five'
# e.g. 11 -> 'eleven'
# e.g. 56 -> 'fifty-six'

# alternatively, use a dictionary: ones = {0:'zero', 1:'one', 2:'two'
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

user_number = int(input('what is the number? '))
if user_number < 10:
    print(ones[user_number])
elif user_number < 20:
    print(teens[user_number-10])
elif user_number < 100:
    tens_digit = user_number // 10
    ones_digit = user_number % 10
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        print(tens[tens_digit] + '-'+ ones[ones_digit])





