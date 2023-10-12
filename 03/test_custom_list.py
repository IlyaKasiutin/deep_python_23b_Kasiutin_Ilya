import unittest
from CustomList import CustomList


class MyTestCase(unittest.TestCase):
    def test_init(self):
        obj = CustomList([])
        self.assertIsInstance(obj, CustomList)
        self.assertEqual(0, len(obj))

    def test_addition_with_equal_length(self):
        obj_a = CustomList([1, 2, 3])
        obj_b = CustomList([6, 7, 8])
        expected = CustomList([7, 9, 11])
        self.assertEqual(expected, obj_a + obj_b)
        self.assertEqual(expected, obj_b + obj_a)
        expected = CustomList([1, 2, 3])
        self.assertEqual(expected, obj_a)

    def test_addition_with_different_length(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = CustomList([6, 7, 8])
        expected = CustomList([7, 9, 11, 4])
        self.assertEqual(expected, obj_a + obj_b)
        self.assertEqual(expected, obj_b + obj_a)

    def test_subtraction_with_equal_length(self):
        obj_a = CustomList([5, 1, 3])
        obj_b = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4])
        self.assertEqual(expected, obj_a - obj_b)
        expected = CustomList([-4, 1, 4])
        self.assertEqual(expected, obj_b - obj_a)

    def test_subtraction_with_different_length(self):
        obj_a = CustomList([5, 1, 3, 7])
        obj_b = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4, 7])
        self.assertEqual(expected, obj_a - obj_b)
        expected = CustomList([-4, 1, 4, -7])
        self.assertEqual(expected, obj_b - obj_a)

    def test_addition_with_list(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = [2, 5]
        expected = CustomList([3, 7, 3, 4])
        self.assertEqual(expected, obj_a + obj_b)
        self.assertEqual(expected, obj_b + obj_a)

    def test_subtraction_with_list(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = [2, 5]
        expected = CustomList([-1, -3, 3, 4])
        self.assertEqual(expected, obj_a - obj_b)
        expected = CustomList([1, 3, -3, -4])
        self.assertEqual(expected, obj_b - obj_a)

    def test_comparison(self):
        obj_a = CustomList([1, 2, 3, 4])
        self.assertEqual(obj_a, CustomList([1, 2, 3, 4]))
        self.assertEqual(obj_a, CustomList([10]))
        self.assertNotEqual(obj_a, CustomList([1, 2]))
        self.assertGreaterEqual(obj_a, CustomList([10]))
        self.assertLessEqual(obj_a, CustomList([10]))
        self.assertGreater(obj_a, CustomList([1, 2, 3]))
        self.assertLess(obj_a, CustomList([11]))

    def test_str(self):
        obj_a = CustomList([1, 2, 3, 4])
        self.assertEqual(f"[1, 2, 3, 4], sum=10", obj_a.__str__())


if __name__ == '__main__':
    unittest.main()
