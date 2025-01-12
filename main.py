import sys
from typing import List, Tuple

from products import Product
from store import Store

class StoreMenu:

    def __init__(self, store):
        self.store = store

    def print_menu(self):
        menu = """
           Store Menu
           ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """
        print(menu)

    def list_all_products(self) -> None:
        products = self.store.get_all_products()
        print("------")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.show()}")
        print("------")

    def total_amount(self) -> None:
        print(f"Total of {self.store.get_total_quantity()} items in store.")

    def make_order(self) -> None:
        self.list_all_products()

        shopping_list = []
        products = self.store.get_all_products()
        print("When you want to finish the order, press Enter.")

        while picked_product := input("Enter the product number (or leave blank to finish): ").strip():
            if not picked_product.isdigit() or not (0 <= (picked_index := int(picked_product) - 1) < len(products)):
                print("Error: Please enter a valid product number.")
                continue

            try:
                picked_quantity = int(input("Enter the quantity: ").strip())
                if picked_quantity > 0:
                    shopping_list.append((products[picked_index], picked_quantity))
                else:
                    print("Error: Quantity must be a positive integer.")
            except ValueError:
                print("Error: Invalid quantity. Please enter a valid number.")

        if shopping_list:
            total_payment = self.store.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total_payment:.2f}")
        else:
            print("No items were ordered.")




    def exit_store(self):
        sys.exit()


    def menu_logic(self, user_input):

        #define user options
        menu_options = {
            "1": lambda: self.list_all_products(),
            "2": lambda: self.total_amount(),
            "3": lambda: self.make_order(),
            "4": lambda: self.exit_store()
        }

        # Get the selected option and call it, or handle invalid input
        if user_input in menu_options:
            menu_options[user_input]()
        else:
            print("Invalid option. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    store_menu = StoreMenu(best_buy)
    while True:
        store_menu.print_menu()
        user_input = input("Please choose a number: ").strip()
        store_menu.menu_logic(user_input)


if __name__ == '__main__':
    main()

