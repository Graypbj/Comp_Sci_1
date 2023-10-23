def print_alpha_characters(input_string):
    alpha_characters = ''.join(char for char in input_string if char.isalpha())
    print("Alphabetic characters from the input:", alpha_characters)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print_alpha_characters(user_input)
