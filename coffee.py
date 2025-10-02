from order import Order

class Coffee:
    all = []

    def __init__(self, name: str): 
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Coffee name must be a string with at least 3 chars")#validations for coffee name 
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

     @name.setter
    def name(self, _):
        raise Exception("Coffee name cannot be changed after creation")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
    @classmethod
    def most_aficionado(cls, coffee):
        """Find the customer who spent the most on a given coffee"""
        spend = {}
        for order in coffee.orders():
            spend[order.customer] = spend.get(order.customer, 0) + order.price
        if not spend:
            return None
        return max(spend, key=spend.get)

