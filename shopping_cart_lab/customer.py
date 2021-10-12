from shopping_cart import ShoppingCart

class Customer:
    def __init__(self):
        self.customer_input = input('Please enter your name: ')
        return

    def customer_cart_info(self):
        self.cart_info = ShoppingCart()
        self.customer_total = ShoppingCart.cart_total(self)
    
    def customer_add(self):
        self.customer_add_product = ShoppingCart.add_product(self)

    def view_cart(self):
        for product in ShoppingCart.products_in_cart:
            print(product)