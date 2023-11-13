class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f'Inventory: {self.bottles} bottles')


if __name__ == "__main__":
    # Create VendingMachine object
    vending_machine = VendingMachine()

    # Purchase drinks
    drinks_to_purchase = int(input("Enter the number of drinks to purchase: "))
    vending_machine.purchase(drinks_to_purchase)

    # Restock bottles
    bottles_to_restock = int(input("Enter the number of bottles to restock: "))
    vending_machine.restock(bottles_to_restock)

    # Report inventory
    vending_machine.report()
