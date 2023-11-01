class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, today_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = today_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print(f'Model year: {self.model_year}')
        print(f'Purchase price: ${self.purchase_price}')
        print(f'Current value: ${self.current_value}')


if __name__ == "__main__":
    user_input_model_year = int(input('Year car was made: '))
    user_input_price = int(input('Original price of car: '))
    user_input_current_year = int(input('Current year: '))

    my_car = Car()  # Creates an instance of the Car class (make an object based on Car class.
    my_car.model_year = user_input_model_year
    my_car.purchase_price = user_input_price
    my_car.calc_current_value(user_input_current_year)
    my_car.print_info()
