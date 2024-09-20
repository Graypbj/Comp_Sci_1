def int_to_binary(user_input):
    """
    Converts the input integer to its binary representation.

    Parameters:
    user_num (int): The integer to be converted to binary.

    Returns:
    str: Binary representation of the input integer.
    """
    if user_input < 0:
        raise ValueError("Input integer must be non-negative.")

    return bin(user_input)[2:]  # [2:] to remove '0b' prefix


# Example usage
user_num = int(input('Please input an integer: '))  # Replace with any desired integer
out_bin = int_to_binary(user_num)
print(f"The binary representation of {user_num} is: {out_bin}")
