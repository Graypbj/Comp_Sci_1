def driving_cost(mpg, dpg, miles):
    cost = float(miles / mpg * dpg)
    return cost


miles_per_gallon = float(input('Please input the miles per gallon: '))
dollars_per_gallon = float(input('Please input the dollars per gallon: '))
miles_driven = float(input('Please input the miles driven: '))

formatted_number = f"{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.3}"
print('The cost of driving', miles_driven, 'is', formatted_number)
