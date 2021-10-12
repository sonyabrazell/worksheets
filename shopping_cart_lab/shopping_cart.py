class ShoppingCart:
    def __init__(self, products_in_cart, product, product_price):
        self.products_in_cart = products_in_cart
        self.product = product
        self.product_price = product_price
        self.products_in_cart = []
        self.product = ''
        self.product_price = ''

    def add_product(self):
        self.products_in_cart.append
        print(self.products_in_cart)

    def cart_total(self):
        self.total_price = self.product * self.product_price
        print(self.total_price)

    def empty_cart(self):
        self.products_in_cart.remove
        print(self.products_in_cart)

