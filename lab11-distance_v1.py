
# lab 11 v1: convert the given distance and units to meters

# 1) get the distance from the user
# 2) convert that distance to a float
# 3) get the units from the user
# 4) convert the distance to meters

# meters = 1609.34*miles
# meters = 0.3048*feet
# meters = 1000*km

# convert the given distance from the given units to meters
def to_meters(distance, units):
    if units == 'm': # meters
        return distance
    elif units == 'mi': # miles
        return distance * 1609.34
    elif units == 'ft': # feet
        return distance * 0.3048
    elif units == 'km': # kilometers
        return distance * 1000

print('Welcome to the Distance Converter 5000™')
distance = float(input('what is the distance? '))
units = input('what are the units? ')
distance_in_m = to_meters(distance, units)
output = str(distance) + ' ' + units + ' is '
output += str(distance_in_m) + ' m'
print(output)
