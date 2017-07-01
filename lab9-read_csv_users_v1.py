
# lab9: load a list of users with their attributes from a CSV
# see peeps.csv for data format
# v1: load all users, and print them out nicely formatted

users = [] #declare users as an empty list
with open('peeps.csv', 'r') as f: #open a file with read access
	header = f.readline().strip().split(',') #take the first line, remove whitespace, and convert it to a list
	for user_str in f: #loop through every line in the e
		user_attributes = user_str.strip().split(',') #remove the whitespace, split it into a list
		user = {} #begin with an empty dictionary
		for i in range(len(header)):
			header_text = header[i] #e.g. 'name', 'favorite color', etc
			user_attribute = user_attributes[i]
			user[header_text] = user_attribute # set the attribute on the user
		users.append(user) # add the user to the list of users

# print the user information
for i,user in enumerate(users): #iterate over both the indices and elements
	print('user '+str(i)) #print 'user 0', 'user 1', etc
	for user_attribute_name in user.keys(): #iterate over the keys of the dictionary representing the user
		user_attribute_value = user[user_attribute_name] #get the value from the key
		print('\t'+user_attribute_name+': '+user_attribute_value) #print the user attribute



