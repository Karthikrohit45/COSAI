def add_item_to_cart(cart, item_name, price):
    """Add an item to the shopping cart."""
    cart[item_name] = price

def view_cart(cart):
    """Display the items in the cart with their prices."""
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, price in cart.items():
            print(f"{item}: ${price:.2f}")

def calculate_total(cart):
    """Calculate the total cost of the items in the cart."""
    total = sum(cart.values())
    return total


if __name__ == "__main__":
    shopping_cart = {}

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Calculate total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            item_name = input("Enter the item name: ")
            price = float(input("Enter the price of the item: $"))
            add_item_to_cart(shopping_cart, item_name, price)
            print(f"{item_name} has been added to your cart.")
        
        elif choice == '2':
            view_cart(shopping_cart)
        
        elif choice == '3':
            total_cost = calculate_total(shopping_cart)
            print(f"Total cost of items in your cart: ${total_cost:.2f}")
        
        elif choice == '4':
            print("Thank you for shopping! Goodbye.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
