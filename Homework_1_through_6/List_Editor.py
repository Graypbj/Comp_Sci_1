# Define my_list and get user inputs for my_flower1, my_flower2, and my_flower3
my_flower1 = input("Enter your first flower: ")
my_flower2 = input("Enter your second flower: ")
my_flower3 = input("Enter your third flower: ")
my_list = [my_flower1, my_flower2, my_flower3]

# Define your_list and get user inputs for your_flower1 and your_flower2
your_flower1 = input("Enter another flower: ")
your_flower2 = input("Enter one more flower: ")
your_list = [your_flower1, your_flower2]

# Concatenate my_list and your_list to create our_list
our_list = my_list + your_list

# Append the user input their_flower to the end of our_list
their_flower = input("Enter yet another flower: ")
our_list.append(their_flower)

# Replace my_flower2 in our_list with their_flower
our_list[1] = their_flower

# Remove the first occurrence of their_flower from our_list without using index()
our_list.remove(their_flower)

# Remove the second element of our_list
del our_list[1]

# Print the final our_list
print("Final our_list:", our_list)
