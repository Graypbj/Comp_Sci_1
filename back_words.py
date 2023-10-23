while True:
    print('Enter q to quite')
    user_input = input('Enter a string: ')
    if 'q' in user_input:
        break
    else:
        # Print the reversed user_input
        print('The reversed string is:', user_input[::-1])

print('goodbye')
