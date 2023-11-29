place_to_hold_numbers = []
while True:
    user_input = input('Enter a number to add to the list or enter q to quit: ')
    if user_input == 'q':
        break
    else:
        user_input = int(user_input)
        if 0 >= user_input:
            place_to_hold_numbers.append(user_input)

place_to_hold_numbers.sort(reverse=True)

print('Our list after sorting: ', place_to_hold_numbers)

for individual_number in place_to_hold_numbers:
    print(individual_number, end=' ')
