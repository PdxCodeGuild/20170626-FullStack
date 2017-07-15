
# lab9 v4: this time, using a class

class Peep:
    def __init__(self, name, age, favorite_color, favorite_fruit):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        self.favorite_fruit = favorite_fruit

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, favorite color: {self.favorite_color}, favorite_fruit: {self.favorite_fruit}'

users = []
with open('peeps.csv', 'r') as f:
    header = f.readline()
    for user_str in f:
        user_attributes = user_str.strip().split(',')

        name = user_attributes[0]
        age = int(user_attributes[1])
        favorite_color = user_attributes[2]
        favorite_fruit = user_attributes[3]

        user = Peep(name, age, favorite_color, favorite_fruit)
        users.append(user)


for i,user in enumerate(users):
    print(str(user))

