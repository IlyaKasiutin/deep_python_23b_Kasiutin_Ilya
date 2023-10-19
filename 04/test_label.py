import unittest
from Label import Label


class Test:
    value = Label((4, 5))


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Test()

    def test_with_correct_value(self):
        self.test.value = 'abcd'
        self.assertEqual('abcd', self.test.value)

    def test_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            self.test.value = '1'

    def test_with_non_str(self):
        with self.assertRaises(TypeError):
            self.test.value = 1

    def test_two_instances(self):
        new_inst = Test()
        self.test.value = 'abcd'
        new_inst.value = 'abcde'
        self.assertEqual('abcd', self.test.value)
        self.assertEqual('abcde', new_inst.value)

    def test_change_value(self):
        self.test.value = 'first'
        self.test.value = 'new_'
        self.assertEqual('new_', self.test.value)

    def test_change_from_correct_to_incorrect(self):
        self.test.value = 'abcd'
        with self.assertRaises(ValueError):
            self.test.value = 'incorrect value'

        self.assertEqual('abcd', self.test.value)

    def test_change_with_two_instances(self):
        new_inst = Test()
        self.test.value = 'first'
        new_inst.value = 'value'
        self.test.value = 'new_v'
        self.assertEqual('new_v', self.test.value)
        self.assertEqual('value', new_inst.value)

        with self.assertRaises(ValueError):
            self.test.value = 'incorrect value'

        self.assertEqual('new_v', self.test.value)
        self.assertEqual('value', new_inst.value)

    def test_init_without_params(self):
        with self.assertRaises(TypeError):
            label_inst = Label()

    def test_incorrect_type_init(self):
        with self.assertRaises(TypeError):
            label_inst = Label([4, 5])

    def test_empty_tuple_init(self):
        with self.assertRaises(ValueError):
            label_inst = Label(tuple())


if __name__ == '__main__':
    unittest.main()
