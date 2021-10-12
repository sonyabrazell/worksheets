from customer import Customer
from product import Product

product_one = Product('apple', 0.75, 'produce')
product_two = Product('cereal', 3.50, 'grocery')
product_three = Product('brownies', 4.00, 'bakery')

customer_one = Customer()
customer_two = Customer()

print(customer_one)

customer_one.customer_add(product_one)
customer_one.customer_add(product_two)
customer_one.customer_add(product_three)

customer_one.view_cart
customer_one.customer_cart_info