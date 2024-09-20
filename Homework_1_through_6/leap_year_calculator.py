input_year = int(input('Please input a year: '))

is_leap_year = input_year % 4

if is_leap_year == 0:
    print('This is a leap year')
else:
    print('This is not a leap year')
