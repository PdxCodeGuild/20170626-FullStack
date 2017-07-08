
# lab9: load a list of users with their attributes from a CSV
# see peeps.csv for data format
# v3: for each user, print a given attribute

def load_users(file_name):
    users = []
    with open(file_name, 'r') as f:
        header = f.readline().strip().split(',')
        for user_str in f: # loop through every line in the text file
            user_attributes = user_str.strip().split(',')
            user = {} # begin with an empty dictionary
            for i in range(len(header)):
                header_text = header[i]
                user_attribute = user_attributes[i]
                user[header_text] = user_attribute # set the attribute on the user
            users.append(user) # add the user to the list of users
    return users

# if user_attribute_value is 'age'
# 'matthew's age is 28'
# 'rob's age is 27'
def print_users_attribute(user_attribute_name, users):
    for user in users:
        user_name = user['name']
        user_attribute_value = user[user_attribute_name]
        message = user_name + '\'s ' + user_attribute_name + ' is ' + user_attribute_value
        print(message)


users = load_users('peeps.csv')
print_users_attribute('age', users)