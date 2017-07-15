
# lab 26: adventure through a 2D grid
# added 'fog of war', randomly generated walls

import random

class Player:
    
    def __init__(self, name, location_i, location_j):
        self.name = name
        self.location_i = location_i
        self.location_j = location_j
        self.health = 5
        self.inventory = []


def print_board(board, player):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if i == player.location_i and j == player.location_j:
                print('☺', end='')
            elif abs(i-player.location_i) <= 1 and abs(j-player.location_j) <= 1:
                print(board[j][i], end='')
            else:
                print('░', end='')
        print()

def cheat(board, player):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if i == player.location_i and j == player.location_j:
                print('☺', end='')
            else:
                print(board[j][i], end='')
        print()


def make_random_wall(board, i, j, direction=''):
    directions = ['north', 'south', 'east', 'west']

    if random.randint(1,10) < 2 or direction=='':
        direction = random.choice(directions)

    if i >= 0 and i < width and j >= 0 and j < height:
        board[j][i] = '█'

        if direction == 'north':
            j -= 1
        elif direction == 'south':
            j += 1
        elif direction == 'east':
            i += 1
        elif direction == 'west':
            i -= 1

        if random.random() < 0.99:
            make_random_wall(board, i, j, direction)


width = 20
height = 20
board = [[' ' for i in range(width)] for j in range(height)]

player = Player('Link', 0, 0)

for i in range(5):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    make_random_wall(board, i, j)


def add_item_to_board(item):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    if board[i][j] == ' ':
        board[i][j] = item
    else:
        add_item_to_board(item)


for k in range(5):
    add_item_to_board('¥')


def check_location(board, player):
    if board[player.location_j][player.location_i] == '¥':
        print('You have encountered an enemy!!!')
        action = input('what do you do? ')
        if action == 'attack':
            print('You have slain the enemy!')
            board[player.location_j][player.location_i] = ' '
        else:
            print('You hesitated, and were killed!')
            exit()


while True:
    command = input('> ')
    if command == 'map':
        print_board(board, player)
    elif command == 'cheat':
        cheat(board, player)
    elif command == 'quit' or command == 'exit':
        print('goodbye')
        break
    elif command == 'north' or command == 'up':
        if player.location_j > 0:
            player.location_j -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'south' or command == 'down':
        if player.location_j < height-1:
            player.location_j += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'east' or command == 'right':
        if player.location_i < width-1:
            player.location_i += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'west' or command == 'left':
        if player.location_i > 0:
            player.location_i -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    else:
        print('I did not recognize that command')
