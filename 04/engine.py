from brand import Brand
from label import Label
from positive_integer import PositiveInteger


class Engine:
    brand = Brand()
    model = Label((4, 5))
    horsepower = PositiveInteger()

    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.brand} {self.model} {self.horsepower} hp."


engine = Engine("Mitsubishi", "4G13", 75)

print(engine)
