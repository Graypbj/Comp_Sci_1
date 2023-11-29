change = int(input('Please input the amount of change: '))

if change < 69:
    print('You don\'t have enough for a chicken nuggy')

dollars = change // 100
change %= 100

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change // 1

if dollars == 1:
    print('1 dollar')
elif dollars > 1:
    print(dollars, 'dollars')

if quarters == 1:
    print('1 quarter')
elif quarters > 1:
    print(quarters, 'quarters')

if dimes == 1:
    print('1 dime')
elif dimes > 1:
    print(dimes, 'dimes')

if nickels == 1:
    print('1 nickel')
elif nickels > 1:
    print(nickels, 'nickels')

if pennies == 1:
    print('1 penny')
elif pennies > 1:
    print(pennies, 'pennies')
