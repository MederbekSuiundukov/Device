
class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def display_info(self):
        return f"Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        self.price *= (1 - discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
        else:
            raise ValueError("Insufficient stock")