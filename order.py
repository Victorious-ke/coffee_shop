#ocurs when a 

from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee


class Order:

    all = []

    def __init__(self, customer, coffee, price: float):
        from customer import Customer
        from coffee import Coffee


              #Customer and Coffee name validations for existng coffee and customer
        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer")


        if not isinstance(coffee, Coffee):
            raise Exception(" coffee must be a Coffee")


        if not isinstance(price, (int, float)):
            raise Exception("Price must be number") #validations for price number and fload

        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _):
        raise Exception("Price cannot be changed after creation")
