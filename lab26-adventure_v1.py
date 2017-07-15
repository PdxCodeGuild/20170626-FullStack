
# lab 26: adventure through a 2D grid

import random


class Player:
    
    def __init__(self, name, location_i, location_j):
        self.name = name
        self.location_i = location_i
        self.location_j = location_j


def print_board(board, player):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if i == player.location_i and j == player.location_j:
                print('X', end='')
            else:
                print(board[j][i], end='')
        print()


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

width = 10
height = 10
board = [[' ' for i in range(width)] for j in range(height)]

for i in range(len(board[0])):
    board[0][i] = '*'



player = Player('Link', 0, 0)

for k in range(5):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    board[j][i] = '¥'

while True:
    command = input('> ')
    if command == 'map':
        print_board(board, player)
    elif command == 'quit' or command == 'exit':
        print('goodbye')
        break
    elif command == 'north':
        if player.location_j > 0:
            player.location_j -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'south':
        if player.location_j < height-1:
            player.location_j += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'east':
        if player.location_i < width-1:
            player.location_i += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'west':
        if player.location_i > 0:
            player.location_i -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    else:
        print('I did not recognize that command')


