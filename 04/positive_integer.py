"""Positive integer class"""


class PositiveInteger:
    """Positive integer"""
    def __set_name__(self, owner, name):
        self.name = f"pos_int_{name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise TypeError("must be int")

        if val <= 0:
            raise ValueError("must be positive")

        return setattr(obj, self.name, val)
