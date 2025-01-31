"""
This script defines the main function to run a store menu system,
allowing users to interact with a store by via StoreMenu class via terminal user input.
"""
import sys
#Loads Store Class and Product Class
from products import Product
from store import Store


class StoreMenu:
    """
    A class to represent the menu system interacting with Store class.

    Attributes:
        store_obj (Store): The store instance that manages inventory and operations.
    """
    def __init__(self, store_obj: Store) -> None:
        """
        Initializes the StoreMenu with a given Store instance.

        Args:
            store_obj (Store): The store instance.
        """
        self.store_obj = store_obj

    def print_menu(self) -> None:
        """
        Displays the store menu options to the user.
        """
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
        """
        Lists all available products in the store along with their details.
        """
        # Retrieve the list of products from the store
        products = self.store_obj.get_all_products()
        print("------")
        # Iterate through products and display them with an index
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.show()}")
        print("------")

    def total_amount(self) -> None:
        """
        Displays the total quantity of all products in the store.
        """
        print(f"Total of {self.store_obj.get_total_quantity()} items in store.")

    def make_order(self) -> None:
        """
        Allows the user to create an order by selecting products and quantities.
        Handles input validation and processes the order through the store.
        """
        # Display all available products
        self.list_all_products()

        shopping_list = []
        products = self.store_obj.get_all_products()
        print("When you want to finish the order, press Enter with empty text.")

        # Continuously prompt the user for product selection
        while picked_product := input("Which product # do you want? ").strip():
            # Validate input for product selection
            if not picked_product.isdigit() or not (0 <= (picked_index := int(picked_product) - 1) < len(products)):
                print("Error: Please enter a valid product number.")
                continue
            # Prompt for quantity and validate it
            try:
                picked_quantity = int(input("What amount do you want? ").strip())
                if picked_quantity > 0:
                    shopping_list.append((products[picked_index], picked_quantity))
                else:
                    print("Error: Amount must be a positive integer.")
            except ValueError:
                print("Error: Invalid Amount. Please enter a valid number.")

        # Process the order if items were added to the shopping list
        if shopping_list:
            try:
                total_payment = self.store_obj.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total_payment:,.2f}")
            except ValueError as e:
                print(f"Order processing error: {e}")
            else:
                print("No items were ordered.")

    def exit_store(self) -> None:
        """
        Exits the store menu system.
        """
        sys.exit()

    def menu_logic(self, user_input: str) -> None:
        """
        Executes the appropriate action based on user input.

        Args:
            user_input (str): The menu option selected by the user.
        """
        # Define the mapping of menu options to functions
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


def main() -> None:
    """
    Sets up the store and initializes the store menu for user interaction.
    """
    # Raw product data
    raw_product_list = [
        {"name": "MacBook Air M2", "price": 1450, "quantity": 100},
        {"name": "MacBook Air M3", "price": -2450, "quantity": 0},  # Invalid: Negative price
        {"name": "Bose QuietComfort Earbuds", "price": 250, "quantity": 500},
        {"name": "Google Pixel 7", "price": 500, "quantity": 250}
    ]

    # validating valid try-except handling
    product_list = []
    for data in raw_product_list:
        try:
            product_list.append(Product(**data))
        except ValueError as e:
            print(f"\nSkipping invalid product: {data} -> {e}")

    # Create a Store instance with the product list
    best_buy = Store(product_list)
    # Initialize the StoreMenu with the Store instance
    store_menu = StoreMenu(best_buy)

    # Display the menu and handle user input in a loop
    while True:
        store_menu.print_menu()
        user_input = input("Please choose a number: ").strip()
        store_menu.menu_logic(user_input)


if __name__ == '__main__':
    main()

