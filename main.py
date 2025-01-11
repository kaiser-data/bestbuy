from products import Product
from store import Store

def start():
    menu = """
       Store Menu
       ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """
    print(menu)

def list_all_products(best_buy):

    [product.show() for product in best_buy.get_all_products()]




def menu_logic (user_input):
    pass


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

    start()
    list_all_products(best_buy)



if __name__ == '__main__':
    main()

