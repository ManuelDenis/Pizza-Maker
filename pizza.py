from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name.isspace():
            raise ValueError("The name cannot be an empty string")
        else:
            self._name = name

    @property
    def dough(self):
        return self._dough

    @dough.setter
    def dough(self, dough):
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self._dough = dough

    @property
    def toppings_capacity(self):
        return self._toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        if toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        else:
            self._toppings_capacity = toppings_capacity

    def add_topping(self, topping: Topping):

        if topping.topping_type in self.toppings:
            if self.toppings_capacity > len(self.toppings):
                self.toppings[topping.topping_type] += topping.weight
            else:
                raise ValueError("Not enough space for another topping")
        else:
            if self.toppings_capacity > len(self.toppings):
                self.toppings[topping.topping_type] = topping.weight
            else:
                raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        total_pizza_weight = 0
        for k, v in self.toppings.items():
            total_pizza_weight += v
        total_pizza = self.dough.weight + total_pizza_weight
        return total_pizza
