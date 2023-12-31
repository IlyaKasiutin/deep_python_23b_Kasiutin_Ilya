"""Brand class implementation"""


class Brand:
    """Brand class (not-null string)"""
    def __set_name__(self, owner, name):
        self.name = f"__brand_{name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise TypeError("must be str")

        if not val:
            raise ValueError("brand can't be empty string")
        return setattr(obj, self.name, val)
