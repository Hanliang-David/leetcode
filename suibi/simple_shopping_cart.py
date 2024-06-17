class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_total(self):
        return sum(self.items.values())

    def display_cart(self):
        for item, price in self.items.items():
            print(f"{item}: ${price}")

def main():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.display_cart()
    print(f"Total: ${cart.get_total()}")

if __name__ == "__main__":
    main()
