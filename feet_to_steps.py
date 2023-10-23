def feet_to_steps(user_feet):
    return int(user_feet / 2.5)


input_feet = float(input('Please input the number of feet: '))
steps_walked = feet_to_steps(input_feet)
print('You have walked', steps_walked, 'steps')
