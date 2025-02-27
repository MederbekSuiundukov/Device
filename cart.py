class Cart:

    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        pair = (device, amount)
        # pair[0] - device
        # pair[1] - amount
        self.items.append(pair)
        self.total_price += device.price * amount

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if item[1] >= amount:
                    item[1] -= amount
                    self.total_price -= device.price * amount
                    device.stock += amount
                    if item[1] == 0:
                        self.items.remove(item)
                else:
                    print(f"Error: Cannot remove {amount} units of {device.name}.")
                return
        print(f"Error: {device.name} not found in the cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device, amount in self.items:
            print(f'{device.name} - {amount} units')

    def checkout(self):
        print("Checkout Summary:")
        self.print_items()
        print(f"Total Price: ${self.total_price}")
        print("Thank you for your purchase!")
        self.items = []
        self.total_price = 0


