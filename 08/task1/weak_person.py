"""Class with weakrefs"""
from typing import Any
import weakref


class Value:
    """Class for holding value of any type"""
    ref_holder = []

    def __init__(self, val: Any):
        self.value = val

        Value.ref_holder.append(self)


class WeakPerson:
    """Class with weak refs"""
    def __init__(self, age: int, height: int, job: str):
        self.age = weakref.ref(Value(age))
        self.height = weakref.ref(Value(height))
        self.job = weakref.ref(Value(job))

    def __getattribute__(self, item):
        if item == '__dict__':
            return super().__getattribute__(item)

        if item in self.__dict__:
            return self.__dict__[item]().value

        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super().__setattr__(key, value)
        else:
            self.__dict__[key]().value = value
