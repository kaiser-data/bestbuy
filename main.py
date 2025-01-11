from typing import List

from products import Product
from store import Store

class StoreMenu:
    def __init__(self, store):
        self.store = store

    def start(self):
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
        products = best_buy.get_all_products()
        print("------")
        [print(f"{i+1}. {products[i].show()}") for i in range(len(products))]
        print("------")

    def total_amount(self) -> None:
        print(f"Total of {best_buy.get_total_quantity()} items in store\n")

    def make_order(self) -> List[Product]:

        shopping_list =[]
        print("When you want to finish order, enter empty text.")
        while True:
            picked_product = input("Which product do you want? ")
            picked_quantity = input("What amount do you want?")
            if picked_product == "":
                return shopping_list
                break
            elif picked_product in best_buy.get_all_products():
                shopping_list.append(picked_product, picked_quantity)
            else:
                print("Error adding product")


    def menu_logic (user_input):
        pass


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    list_all_products()

    user_input = input("Please choose a number: ")

    start()



if __name__ == '__main__':
    main()

