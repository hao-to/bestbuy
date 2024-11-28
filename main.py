from products import Product
from store import Store

def main():
    # create products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    # create a Store
    store = Store([bose, mac])
    print("\n--- Store created with initial products ---")
    for product in store.get_all_products():
        print(product.show())

    # add product (pixel)
    store.add_product(pixel)
    print("\n--- Added Pixel to store ---")
    for product in store.get_all_products():
        print(product.show())

    # remove product (mac)
    store.remove_product(mac)
    print("\n--- Removed MacBook Air from store ---")
    for product in store.get_all_products():
        print(product.show())

    # show total qty in store
    print("\n--- Total quantity in store ---")
    print(f"Total quantity in store: {store.get_total_quantity()}")

    # place a test order
    print("\n--- Placing a test order ---")
    shopping_list = [
        (bose, 50),  # buy 50 Bose
        (pixel, 2),  # buy 2 Pixels
        (mac, 10)  # should raise error: mac was removed
    ]
    total_price = store.order(shopping_list)
    print(f"Total price of the order: {total_price}")

    # Final overview of the store
    print("\n--- Final Store Overview ---")
    for product in store.get_all_products():
        print(product.show())
    print(f"Final total quantity in store: {store.get_total_quantity()}")


if __name__ == "__main__":
    main()
