
# lab 11 v2: convert the given distance and units to the target units
# we have four types of units: meters (m), miles (mi), feet (ft), and kilometers (km)
# we could handle each case individually
#     e.g. if from_units == 'm' and to_units == 'miles'
# instead, we'll just convert to meters, then convert to the target units

# 1) get the distance from the user
# 2) convert that distance to a float
# 3) get the units for that distance from the user
# 4) get the units that the user wants to convert to
# 4) convert the distance to meters
# 5) convert the distance from meters to the target

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

# convert the given distance (in meters) to the target units
def from_meters(distance, units):
    if units == 'm': # meters
        return distance
    elif units == 'mi': # miles
        return distance / 1609.34
    elif units == 'ft': # feet
        return distance / 0.3048
    elif units == 'km': # kilometers
        return distance / 1000

print('Welcome to the Distance Converter 5001™')
distance_in = float(input('what is the distance? '))
units_in = input('what are the units you\'re converting from? ')
units_out = input('what are the units you\'re converting to? ')
distance_in_m = to_meters(distance_in, units_in)
distance_out = from_meters(distance_in_m, units_out)
output = str(distance_in) + ' ' + units_in + ' is '
output += str(distance_out) + ' ' + units_out
print(output)
