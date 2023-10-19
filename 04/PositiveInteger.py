class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = f"pos_int_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if obj is None:
            return None

        if not isinstance(val, int):
            raise TypeError("must be int")

        if val <= 0:
            raise ValueError("must be positive")

        return setattr(obj, self.name, val)
