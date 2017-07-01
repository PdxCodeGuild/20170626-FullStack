
# lab 3: for a given dollar amount, figure out the number of each coin
# first we get the dollar amount from the user, and convert it into cents
# then we begin breaking that amount down, starting with the highest value coin
# and ending with pennies

user_input = input("Enter the total value: $") # we're expecting a value like 1.26
value = int(float(user_input)*100) #convert $ amount to total number of cents

half_dollar = {'name':'half-dollar', 'value':50, 'count':0}
quarter = {'name':'quarter', 'value':25, 'count':0}
dime = {'name':'dime', 'value':10, 'count':0}
nickel = {'name':'nickel', 'value':5, 'count':0}
penny = {'name':'penny', 'value':1, 'count':0}
coins = [half_dollar, quarter, dime, nickel, penny]

for i,coin in enumerate(coins):	#loop over both indices and elements
	if value >= coin['value']:
		coin['count'] = value // coin['value']
		value -= coin['count']*coin['value']
	message = coin['name'] + ' - ' + str(coin['count'])
	print(message)




