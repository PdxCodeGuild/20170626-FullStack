
# lab9: load a list of users with their attributes from a CSV
# see peeps.csv for data format
# v2: allow the terminal user to search for a given user by name
# if it's found, print out their data

def load_users(file_name):
    users = []
    with open(file_name, 'r') as f:
        header = f.readline().strip().split(',')
        print(header)
        for user_str in f: # loop through every line in the text file
            user_attributes = user_str.strip().split(',')
            user = {} # begin with an empty dictionary
            for i in range(len(header)):
                header_text = header[i]
                user_attribute = user_attributes[i]
                user[header_text] = user_attribute # set the attribute on the user
            users.append(user) # add the user to the list of users
    return users

# returns a user with the given name
# or none if a user with that name isn't found
def find_user(user_name, users):
    for user in users:
        if user_name == user['name']:
            return user
    return None


users = load_users('peeps.csv')

print('Welcome to the User Manager 5000')
print('input \'done\' if done')

# keep asking the terminal user which user's information
# they'd like to see, then ask which attribute they'd like to know
while True:
    user_name = input('which user would you like to see? ')
    if user_name == 'done':
        break
    
    user = find_user(user_name, users)
    if user is None:
        print('user not found')
    else:
        #print(user)
        #print(list(user.keys()))
        user_attribute_name = input('which attribute would you like to know? ')
        if user_attribute_name == 'all':
            print(user)
        else:
            user_attribute_value = user[user_attribute_name]
            print(user_attribute_value)





