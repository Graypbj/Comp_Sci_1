def brute_force_solver(a1, b1, c1, a2, b2, c2):
    # Iterate through all possible values of x and y
    for x in range(-10, 11):
        for y in range(-10, 11):
            # Check if the current x and y satisfy both equations
            if (a1 * x + b1 * y == c1) and (a2 * x + b2 * y == c2):
                return f'x = {x}, y = {y}'

    return 'There is no solution'


# Input coefficients for the equations
a1 = int(input('A1: '))
b1 = int(input('B1: '))
c1 = int(input('C1: '))
a2 = int(input('A2: '))
b2 = int(input('B2: '))
c2 = int(input('C2: '))

# Solve the equations using brute force
solution = brute_force_solver(a1, b1, c1, a2, b2, c2)

# Output the result
print(solution)
