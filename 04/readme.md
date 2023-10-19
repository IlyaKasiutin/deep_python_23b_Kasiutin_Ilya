# Пояснение к дескрипторам
Предполагается для использования в, например, маркировке двигателей.
Каждый двигатель имеет производителя (Brand), модель (Label) и количество лошадиных сил (PositiveInteger)

Например, реализация класса Engine может быть такой:
```python
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
```

```python
>>> print(engine)
>>> Mitsubishi 4G13 75 hp.
```