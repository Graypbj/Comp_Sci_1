name = input('Input a name: ')
place = input('Input a place: ')
number = int(input('Input a number: '))
thing = input('Input a singular noun: ')

if number > 1:
    thing += 's'

print(name.upper(), 'went to', place.upper(), 'to buy', number, thing.upper())
