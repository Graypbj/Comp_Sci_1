place_to_hold_our_numbers = []

user_input = 0
while True:
    user_input = input('Enter a number to add to the list, enter q to quit: ')
    if user_input == 'q':
        break
    else:
        place_to_hold_our_numbers.append(user_input)

# Loop through all the numbers and make them floats
for index in range(len(place_to_hold_our_numbers)):
    initial_number = place_to_hold_our_numbers[index]
    place_to_hold_our_numbers[index] = float(initial_number)
    value_after_conversion = place_to_hold_our_numbers[index]

max_number = max(place_to_hold_our_numbers)
print('Our max number was: ', max_number)

sum_of_our_number = sum(place_to_hold_our_numbers)
print('The sum of our numbers: ', sum_of_our_number)
length_of_our_number = len(place_to_hold_our_numbers)
print('We had this many numbers: ', length_of_our_number)

average_number = sum_of_our_number / length_of_our_number
print('Our average is: ', average_number)
