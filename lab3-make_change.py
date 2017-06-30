
# lab 3: for a given dollar amount, figure out the number of each coin
# first we get the dollar amount from the user, and convert it into cents
# then we begin breaking that amount down, starting with the highest value coin
# and ending with pennies


user_input = input("Enter the total value: $") # we're expecting a value like 1.00
value = int(float(user_input)*100) #convert $ amount to total number of cents

# declare variables, initialize to 0
n_quarters = 0
n_dimes = 0
n_nickles = 0
n_pennies = 0

if value >= 25: #if we can squeeze at least one quarter out
    n_quarters = value // 25 #find how many we can get
    value -= n_quarters*25 #subtract that value from the total
if value >= 10:
    n_dimes = value // 10
    value -= n_dimes*10
if value >= 5:
    n_nickles = value // 5
    value -= n_nickles*5
n_pennies = value #break whatever's left into pennies

print('Quarters: ', n_quarters)
print('Dimes: ', n_dimes)
print('Nickles: ', n_nickles)
print('Pennies: ', n_pennies)


