class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self._topping_type

    @topping_type.setter
    def topping_type(self, topping_type):
        if topping_type.isspace():
            raise ValueError("The topping type cannot be an empty string")
        else:
            self._topping_type = topping_type

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self._weight = weight
