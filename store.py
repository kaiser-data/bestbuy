from typing import List, Tuple
from products import Product  # Assuming Product class is defined in the `products` module


# Store class

class Store:
    def __init__(self, product_list: List[Product]):
        self.product_list = product_list
    """
    Initializes the Store class with a list of products.
    """

    def add_product(self, product):
        """
        Adds a product Class Object to the store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        """
        self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.
        """
        return sum(product.quantity for product in self.product_list)

    def get_all_products(self):
        """
        Returns all active products in the store.
        """
        return [product for product in self.product_list if product.is_active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order and returns the total price.
        Deducts the quantities of the ordered products.
        """
        total_price = 0.0
        active_products = self.get_all_products()

        for product, quantity in shopping_list:
            if product in active_products:
                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"Error buying {product.name}: {e}")
            else:
                raise ValueError(f"Product {product.name} is not available in the store.")
        return total_price


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))
