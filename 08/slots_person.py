"""Class with slots"""


class SlotsPerson:
    __slots__ = ('age', 'height', 'job')

    def __init__(self, age: int, height: int, job: str):
        self.age = age
        self.height = height
        self.job = job
