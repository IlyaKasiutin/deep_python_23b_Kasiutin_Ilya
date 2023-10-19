import unittest
from PositiveInteger import PositiveInteger


class Test:
    value = PositiveInteger()


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Test()

    def test_correct_input(self):
        self.test.value = 10
        self.assertEqual(10, self.test.value)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            self.test.value = 0

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.test.value = -1

    def test_non_int_input(self):
        with self.assertRaises(TypeError):
            self.test.value = "string"
            self.test.value = 10.5

    def test_two_instances(self):
        new_inst = Test()
        self.test.value = 10
        new_inst.value = 20
        self.assertEqual(10, self.test.value)
        self.assertEqual(20, new_inst.value)

    def test_change_value(self):
        self.test.value = 10
        self.test.value = 20
        self.assertEqual(20, self.test.value)

    def test_change_from_correct_to_incorrect(self):
        self.test.value = 10
        with self.assertRaises(ValueError):
            self.test.value = -1

        self.assertEqual(10, self.test.value)

    def test_change_with_two_instances(self):
        new_inst = Test()
        self.test.value = 10
        new_inst.value = 20
        self.test.value = 30
        self.assertEqual(30, self.test.value)
        self.assertEqual(20, new_inst.value)

        with self.assertRaises(ValueError):
            self.test.value = -1

        self.assertEqual(30, self.test.value)
        self.assertEqual(20, new_inst.value)


if __name__ == '__main__':
    unittest.main()
