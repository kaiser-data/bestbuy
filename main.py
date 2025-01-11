import products
import store

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

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start()

if __name__ == '__main__':
    main()

