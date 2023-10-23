# Get users name
name = input('Please input your name: ')

# Get MPG from user
mpg = float(input('Please input the miles per gallon of your vehicle: '))

# Get cost of gas per gallon
gas_price = float(input('What is the current cost of gas per gallon: '))

# Where would you like to travel to? Oklahoma City, New York City, The Nether
destination = int(input('Where would you like to go?\nOklahoma City(1)\nNew York City(2)\nThe Nether(3)\n'))

# Distances driven
if destination == 1:
    distance = 70
    place = 'Oklahoma City'
if destination == 2:
    distance = 1520
    place = 'New York City'
if destination == 3:
    distance = 500000
    place = 'The Nether'

# Calculate cost of driving
cost = distance / mpg * gas_price

# Output the variables input
print('Hello, ', name, 'it will cost you', format(cost, '.2f'), 'to get to', place)
