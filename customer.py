from order import Order

#create class 
class Customer:
  all = []

  def __init__(self, name: str):
    self.name = name
    Customer.all.append(self)

    @property
    def name(self):
      return self._name

    