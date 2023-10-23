def word(alpha_input):
    alpha_characters = ''.join(char for char in alpha_input if char.isalpha())
    return alpha_characters


def number(number_input):
    num_characters = ''.join(char for char in number_input if char.isnumeric())
    return num_characters


def get_input():
    typed = input("Please input an object and a number, to quit type quit 0: ")
    return typed


if __name__ == '__main__':
    user_input = ''
    while user_input != 'quit 0':
        user_input = get_input()
        num = number(user_input)
        thing = word(user_input)
        print('You ate', num, thing, 'while on vacation')
