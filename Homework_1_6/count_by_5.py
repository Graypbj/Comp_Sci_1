
while True:
    try:
        first_number = int(input("Input a number: "))
        second_number = int(input("Input a number greater than the first: "))

        if first_number >= second_number:
            print("Second integer can't be less than the first.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer")

# Create while statement that compares the two numbers that prints and increases the first number by 5
while first_number <= second_number:
    print(first_number)
    first_number += 5
