class Product:

    def __init__(self, name, price, quantity):
        if name == '' or price < 0 or quantity < 0:
            raise ValueError('Name cannot be empty and price or quantity cannot be negative')

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True



    def get_quantity(self) -> float:
        return self.quantity



    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()



    def is_active(self) -> bool:
        return self.quantity == True

    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        print(f" {self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, purchase_quantity) -> float:
        if purchase_quantity <= 0:
            raise ValueError('Quantity to buy must be greater than zero')
        if self.quantity >= purchase_quantity:
            self.quantity -= purchase_quantity
            return self.price * purchase_quantity
        else:
            raise ValueError('Not enough quantity in stock')
