import unittest
from CustomMeta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = CustomClass()

    def test_class_variable(self):
        self.assertEqual(50, CustomClass.custom_x)

        with self.assertRaises(AttributeError):
            self.assertEqual(50, CustomClass.x)

    def test_instance_variable(self):
        self.assertEqual(50, self.instance.custom_x)

        with self.assertRaises(AttributeError):
            self.assertEqual(50, self.instance.x)

    def test_init_variable(self):
        self.assertEqual(99, self.instance.custom_val)

        with self.assertRaises(AttributeError):
            self.assertEqual(99, self.instance.val)

    def test_method(self):
        self.assertEqual(100, self.instance.custom_line())

        with self.assertRaises(AttributeError):
            self.assertEqual(100, self.instance.line())

    def test_magic_method(self):
        self.assertEqual("Custom_by_metaclass", str(self.instance))

        with self.assertRaises(AttributeError):
            self.assertEqual("Custom_by_metaclass", self.str())

    def test_dynamic_variable(self):
        self.instance.dynamic = "added later"
        self.assertEqual("added later", self.instance.custom_dynamic)

        with self.assertRaises(AttributeError):
            self.assertEqual("added later", self.instance.dynamic)


if __name__ == '__main__':
    unittest.main()
