import store
import products


def create_shopping_list(store_instance):
    """
    Allows the user to create a shopping list by selecting products and quantities.

    Args:
    store (Store): The store instance containing available products.

    Returns:
    list: A list of tuples, where each tuple contains a product and the quantity to order.
    """
    shopping_list = []
    while True:
        requested_item = input("Which product do you want to order? ")
        if not requested_item:
            print("Please enter a product name: ")
            continue

        # look for product
        for product in store_instance.get_all_products():
            if requested_item.lower() in product.name.lower():
                while True:
                    try:
                        requested_qty = int(input(f"How many {product.name} do you want to order? "))
                        if requested_qty <= 0:
                            print("Quantity must be greater than zero. Please enter a valid number.")
                            continue
                        if requested_qty > product.get_quantity():
                            print("The quantity you want to order exceeds our stock. Please try again.")
                            continue
                        shopping_list.append((product, requested_qty))
                        print(f"Added {requested_qty} of {product.name} to your shopping list.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number")
                break  # product found, exit loop
        else:
            print(f"{requested_item} is not available in store")

        # ask for more items
        while True:
            more_items = input("Do you want to add more products? (Y/N): ").lower()
            if not more_items:  # checking if input is empty
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                continue
            elif more_items == "y":
                break  # return to order
            elif more_items == "n":
                return shopping_list
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


def start(store_instance):
    """
    Displays a menu to the user and handles user input to interact with the store.

    Args:
    store (Store): The store instance containing available products.

    Returns:
    None
    """
    welcome_message = "\nStore Menu"
    print(welcome_message)
    print("-" * len(welcome_message))

    while True:
        print("\n1. List all products\n2. Show total amount in Store\n3. Make an order\n4. Quit")
        try:
            user_choice = int(input("Please enter a number (1 - 4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4. ")
            continue

        if user_choice not in range(1, 5):
            print("Invalid input. Please enter a number between 1 and 4. ")
            continue

        if user_choice == 1:
            items = store_instance.get_all_products()
            print()
            print("*** HERE IS WHAT WE HAVE IN STORE: ***")
            for product in items:
                print(product.show())
        elif user_choice == 2:
            print()
            total_quantity = store_instance.get_total_quantity()
            print(f"*** THERE ARE {total_quantity} PRODUCTS AVAILABLE. ***")
        elif user_choice == 3:
            print()
            shopping_list = create_shopping_list(store_instance)
            total_price = store_instance.order(shopping_list)
            print()
            print(f"Total price of your order: {total_price}")

        elif user_choice == 4:
            print("Bye-bye!")
            break


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = store.Store(product_list)

    # start the program
    start(best_buy)


if __name__ == "__main__":
    main()
