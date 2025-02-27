from smartphone import Smartphone
from cart import Cart
from tablet import Tablet
from laptop import Laptop
def main():
    # Create devices
    devices = [
        Smartphone("iPhone 13", 799, 10, 12, 6.1, 24),
        Laptop("MacBook Pro", 1999, 5, 24, 16, 3.2),
        Tablet("iPad Pro", 1099, 8, 12, "2048x1536", 500),
        Smartphone("iPhone 13", 999.99, 10, 12, 6.1, 20),
        Smartphone("Samsung Galaxy S21", 799.99, 15, 12, 6.2, 22),
        Smartphone("Google Pixel 6", 599.99, 8, 12, 6.4, 24),
        Smartphone("OnePlus 9", 729.99, 12, 12, 6.55, 25),
        Smartphone("Xiaomi Mi 11", 749.99, 5, 12, 6.81, 22),
        Laptop("MacBook Pro 16", 2399.99, 7, 24, 16, 2.3),
        Laptop("Dell XPS 13", 1399.99, 10, 24, 8, 3.0),
        Laptop("HP Spectre x360", 1499.99, 6, 24, 16, 2.8),
        Laptop("Lenovo ThinkPad X1", 1599.99, 4, 24, 16, 3.1),
        Laptop("Asus ROG Zephyrus", 1999.99, 3, 24, 32, 3.6),
        Tablet("iPad Air", 599.99, 10, 12, "2360x1640", 460),
        Tablet("Samsung Galaxy Tab S7", 649.99, 8, 12, "2560x1600", 498),
        Tablet("Microsoft Surface Pro 7", 749.99, 5, 12, "2736x1824", 775),
        Tablet("Lenovo Tab P11", 249.99, 15, 12, "2000x1200", 480),
        Tablet("Amazon Fire HD 10", 149.99, 20, 12, "1920x1200", 465),
        Smartphone("Sony Xperia 1 III", 1299.99, 4, 12, 6.5, 24),
        Smartphone("Nokia 8.3", 699.99, 6, 12, 6.81, 24),
        Laptop("Acer Swift 3", 899.99, 10, 24, 8, 4.0),
        Laptop("Razer Blade 15", 2499.99, 2, 24, 16, 2.6),
        Tablet("Huawei MatePad Pro", 499.99, 5, 12, "2560x1600", 460),
    ]

    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Remove Item from Cart")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Devices:")
            for i, device in enumerate(devices):
                print(f"{i + 1}. {device}")
            try:
                device_choice = int(input("Enter the device number to add to cart: ")) - 1
                if device_choice < 0 or device_choice >= len(devices):
                    print("Invalid device number. Please try again.")
                    continue
                amount = int(input("Enter the quantity: "))
                if amount <= 0:
                    print("Quantity must be a positive number.")
                    continue
                if devices[device_choice].is_available(amount):
                    cart.add_device(devices[device_choice], amount)
                    print(f"{amount} unit(s) of {devices[device_choice].name} added to cart.")
                else:
                    print(f"Error: Not enough stock for {devices[device_choice].name}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            print("\nYour Cart:")
            cart.print_items()
            print(f"Total Price: ${cart.get_total_price()}")
            if cart.items:  # Only show checkout option if cart is not empty
                checkout_choice = input("Do you want to checkout? (y/n): ")
                if checkout_choice.lower() == "y":
                    cart.checkout()

        elif choice == "3":
            if not cart.items:
                print("Your cart is empty.")
            else:
                print("\nItems in Cart:")
                cart.print_items()
                try:
                    device_name = input("Enter the name of the device to remove: ")
                    device_to_remove = None
                    for device, _ in cart.items:
                        if device.name.lower() == device_name.lower():
                            device_to_remove = device
                            break
                    if device_to_remove:
                        amount = int(input("Enter the quantity to remove: "))
                        cart.remove_device(device_to_remove, amount)
                        print(f"{amount} unit(s) of {device_to_remove.name} removed from cart.")
                    else:
                        print("Device not found in cart.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()