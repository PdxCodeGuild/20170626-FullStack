
# lab9: load a list of users with their attributes from a CSV
# see peeps.csv for data format
# Zack's implementation, use csv module, dict and zip

import csv # use the csv module to parse the csv file

users = []
with open('peeps.csv', 'r') as f:
    people = csv.reader(f)
    field_names = next(people)
    for person in people:
        # zip takes an element from each list, and puts it in a tuple
        # e.g. zip(['a', 'b', 'c'], [1,2,3]) returns [('a',1),('b',2),('c',3)]
        # dict converts that list of tuples into a dict
        user = dict(zip(field_names, person))
        users.append(user)
        
print(users)
