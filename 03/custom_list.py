"""Custom list implementation"""


class CustomList(list):
    """List-inherited class with overloaded arithmetics and comparison"""

    def __add__(self, other):
        arr_a = self.copy()
        arr_b = other.copy()
        len_a = len(arr_a)
        len_b = len(arr_b)
        arr_a.extend([0] * (len_b - len_a))
        arr_b.extend([0] * (len_a - len_b))
        return CustomList([sum(elem) for elem in zip(arr_a, arr_b)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        arr_a = self.copy()
        arr_b = other.copy()
        len_a = len(arr_a)
        len_b = len(arr_b)
        arr_a.extend([0] * (len_b - len_a))
        arr_b.extend([0] * (len_a - len_b))
        return CustomList([elem[0] - elem[1] for elem in zip(arr_a, arr_b)])

    def __rsub__(self, other):
        arr_a = self.copy()
        arr_b = other.copy()
        len_a = len(arr_a)
        len_b = len(arr_b)
        arr_a.extend([0] * (len_b - len_a))
        arr_b.extend([0] * (len_a - len_b))
        return CustomList([elem[0] - elem[1] for elem in zip(arr_b, arr_a)])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __str__(self):
        return f"{list(self)}, sum={sum(self)}"
