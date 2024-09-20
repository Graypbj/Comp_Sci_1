def trapezoidal_rule(a, b, n, function):
    """
    Compute the definite integral of a function using the trapezoidal rule.

    Parameters:
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of trapezoids to use for approximation.
    function (function): The function to integrate.

    Returns:
    float: Approximated value of the definite integral.
    """
    h = (b - a) / n
    integral_sum = 0.5 * (function(a) + function(b))

    for i in range(1, n):
        x_i = a + i * h
        integral_sum += function(x_i)

    integral_sum *= h
    return integral_sum


def get_user_input():
    """Get user input for the function, lower limit, upper limit, and number of trapezoids."""
    function_str = input("Enter the function to integrate (e.g., 'x**2'): ")
    function = lambda x: eval(function_str)
    a = float(input("Enter the lower limit (a): "))
    b = float(input("Enter the upper limit (b): "))
    n = int(input("Enter the number of trapezoids (n): "))
    return function, a, b, n


if __name__ == "__main__":
    # Get user input for the function, lower limit, upper limit, and number of trapezoids
    function, lower_limit, upper_limit, num_trapezoids = get_user_input()

    # Compute the integral using the trapezoidal rule
    approximated_integral = trapezoidal_rule(lower_limit, upper_limit, num_trapezoids, function)

    print("Approximated integral:", approximated_integral)
