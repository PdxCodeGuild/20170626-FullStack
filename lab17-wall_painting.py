
# lab 17: wall painting
# ask the user for the width and height of a wall
# ask the user for the cost of a gallon of paint
# one gallon of paint covers 400 square meters
# calculate the total number of gallons required, and the total cost
# v2: you can only buy whole gallons of paint

import math

width = float(input('what is the width of the wall? '))
height = float(input('what is the height of the wall? '))
gallon_paint_cost = float(input('what is the cost of a gallon of paint? $'))

area = width * height
gallons_of_paint = math.ceil(area / 400) # ceiling function

# alternatively, you can perform a 'ceil' the hard way
# gallons_of_paint = area / 400
# if gallons_of_paint-int(gallons_of_paint) > 0:
#     gallons_of_paint = int(gallons_of_paint) + 1
# else:
#     gallons_of_paint = int(gallons_of_paint)

total_cost = gallons_of_paint * gallon_paint_cost
print('gallons of paint: ' + str(gallons_of_paint))
print('total cost: $' + str(total_cost))



