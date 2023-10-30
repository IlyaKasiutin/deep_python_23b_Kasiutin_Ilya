import unittest
from brand import Brand


class Test:
    value = Brand()


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Test()

    def test_with_correct_value(self):
        self.test.value = "Some brand"
        self.assertEqual("Some brand", self.test.value)

    def test_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.test.value = ""

    def test_with_non_str_value(self):
        with self.assertRaises(TypeError):
            self.test.value = 10

    def test_change_value(self):
        self.test.value = "Old value"
        self.test.value = "New value"
        self.assertEqual("New value", self.test.value)

    def test_with_two_instances(self):
        new_inst = Brand()
        self.test.value = "First value"
        new_inst.value = "Second value"
        self.assertEqual("First value", self.test.value)
        self.assertEqual("Second value", new_inst.value)

    def test_change_from_correct_to_incorrect(self):
        self.test.value = "Correct value"
        with self.assertRaises(TypeError):
            self.test.value = -1
        self.assertEqual("Correct value", self.test.value)

    def test_change_with_two_instances(self):
        new_inst = Test()
        self.test.value = "Self"
        new_inst.value = "new_inst"
        self.test.value = "new value"
        self.assertEqual("new value", self.test.value)
        self.assertEqual("new_inst", new_inst.value)

        with self.assertRaises(TypeError):
            self.test.value = 3.14

        self.assertEqual("new value", self.test.value)
        self.assertEqual("new_inst", new_inst.value)

    def test_two_class_instances(self):
        class Foo:
            value1 = Brand()
            value2 = Brand()

        Foo.value1 = "val1"
        Foo.value2 = "val2"
        self.assertEqual("val1", Foo.value1)
        self.assertEqual("val2", Foo.value2)


if __name__ == '__main__':
    unittest.main()
