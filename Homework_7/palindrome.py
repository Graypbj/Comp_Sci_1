def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = ''.join(s.split()).lower()
    return s == s[::-1]


if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")

    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")
