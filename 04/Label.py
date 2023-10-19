class Label:
    def __init__(self, lengths):
        if not len(lengths):
            raise ValueError("lengths must content at least one value")
        if not isinstance(lengths, tuple):
            raise TypeError("lengths must be tuple")
        self.lengths = lengths

    def __set_name__(self, owner, name):
        self.name = f"label_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if obj is None:
            return None

        if not isinstance(val, str):
            raise TypeError("must be str")
        if len(val) not in self.lengths:
            raise ValueError(f"length must be in {self.lengths}")

        return setattr(obj, self.name, val)
