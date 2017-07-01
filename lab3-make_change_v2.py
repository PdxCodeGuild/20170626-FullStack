
# lab 3: for a given dollar amount, figure out the number of each coin
# first we get the dollar amount from the user, and convert it into cents
# then we begin breaking that amount down, starting with the highest value coin
# and ending with pennies

user_input = input("Enter the total value: $") # we're expecting a value like 1.26
value = int(float(user_input)*100) #convert $ amount to total number of cents

coin_values = [50, 25, 10, 15, 2, 1] # the values of each type of coin
coin_counts = [0]*len(coin_values) # the counts of each type of coin, initialized to 0

coin_values.sort() # sort the coin values in ascending order
coin_values.reverse() # reverse the list to put it in descending order

for i,coin_value in enumerate(coin_values):	#loop over both indices and elements
	if value >= coin_value:
		coin_counts[i] = value // coin_value
		value -= coin_counts[i]*coin_value
	
	message = str(coin_value) + '¢ - ' + str(coin_counts[i])
	print(message)


