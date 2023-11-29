# This program takes any number of inputs, multiplies them, prints the output as a rounded number to one decimal point.

# Initialize multiplication
multiplication = 1

# Ask user how many numbers they would like to multiply
num_of_nums = int(input('How many numbers would you like to multiply: '))

# Multiply all inputted numbers by multiplication and get next number
while num_of_nums > 0:
    num_of_nums -= 1
    num = float(input('Please enter a number: '))
    multiplication *= num

print(format(multiplication, '.0f'))
