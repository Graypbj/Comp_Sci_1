import math

while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        if number.is_integer():
            number = int(number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer or float.")

square_root = math.sqrt(number)

print('The square root of', number, 'is', format(square_root, ".2f"))
