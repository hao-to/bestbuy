import products


class Store:
    def __init__(self, list_of_products=None):
        if list_of_products is None:
            list_of_products = []
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.list_of_products:
                print(f"Error: {product.name} is currently not available in the store.")
                continue  # go to next product to be ordered
            if not product.is_active():
                print(f"Error: {product.name} is currently not active (available) and need to be replenished.")
                continue  # disregard inactive products
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Error with product '{product.name}': {e}")
        return total_price
