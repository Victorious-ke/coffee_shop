from order import Order


class Customer:
  all = []

  def __init__(self, name: str):
    self.name = name
    Customer.all.append(self)

    @property
    def name(self):
      return self._name

      @name.setter
      def name(self, value):
        if not isinstance(value, str):
          raise Exception ("Name must be a string")
        if not (1 <=len(value) <= 15):
          
