#ocurs when a 

class Order:

    all = []

    def __init__(self, customer, coffee, price: float):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise Exception("Invalid customer")
        if not isinstance(coffee, Coffee):
            raise Exception("Invalid coffee")
        if not isinstance(price, (int, float)):
            raise Exception("Price must be numeric")

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
