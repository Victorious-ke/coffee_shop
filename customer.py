from coffee_shop.order import Order

#create class 
class Customer:
  all = []

  def __init__(self, name: str):
    self.name = name
    Customer.all.append(self)

    @property
    def name(self):
      return self._name

    @name.setter       #validations for name length and exceptions 
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value
    def orders(self):
        """All orders for this customer"""
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        """Unique list of coffees purchased"""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price: float):
        """Create a new Order linked to this customer"""
        return Order(self, coffee, price)


    