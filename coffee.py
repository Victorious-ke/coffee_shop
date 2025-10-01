from order import Order

class Coffee:
    all = []

    def __init__(self, name: str): 
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Coffee name must be a string with at least 3 chars")
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

     @name.setter
    def name(self, _):
        raise Exception("Coffee name cannot be changed after creation")