import unittest
from custom_list import CustomList


def comp_list(list_a, list_b):
    assert(len(list_a) == len(list_b))

    for elem in zip(list_a, list_b):
        assert(elem[0] == elem[1])
    return True


class MyTestCase(unittest.TestCase):
    def test_init(self):
        obj = CustomList([])
        self.assertIsInstance(obj, CustomList)
        self.assertEqual(0, len(obj))

    def test_equal(self):
        obj_a = CustomList([1, 2, 3])
        obj_b = CustomList([2, 4])
        self.assertEqual(obj_a, obj_b)

    def test_addition_with_equal_length_cl(self):
        obj_a = CustomList([1, 2, 3])
        obj_b = CustomList([6, 7, 8])
        expected = CustomList([7, 9, 11])
        comp_list(expected, obj_a + obj_b)
        comp_list(expected, obj_b + obj_a)
        expected = CustomList([1, 2, 3])
        comp_list(expected, obj_a)
        expected = CustomList([6, 7, 8])
        comp_list(expected, obj_b)

    def test_addition_with_smaller_cl(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = CustomList([6, 7, 8])
        expected = CustomList([7, 9, 11, 4])
        comp_list(expected, obj_a + obj_b)
        comp_list(expected, obj_b + obj_a)
        expected = CustomList([1, 2, 3, 4])
        comp_list(expected, obj_a)
        expected = CustomList([6, 7, 8])
        comp_list(expected, obj_b)

    def test_addition_with_loger_cl(self):
        obj_a = CustomList([6, 7, 8])
        obj_b = CustomList([1, 2, 3, 4])
        expected = CustomList([7, 9, 11, 4])
        comp_list(expected, obj_a + obj_b)
        comp_list(expected, obj_b + obj_a)
        expected = CustomList([6, 7, 8])
        comp_list(expected, obj_a)
        expected = CustomList([1, 2, 3, 4])
        comp_list(expected, obj_b)

    def test_subtraction_with_equal_length(self):
        obj_a = CustomList([5, 1, 3])
        obj_b = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4])
        comp_list(expected, obj_a - obj_b)
        expected = CustomList([-4, 1, 4])
        comp_list(expected, obj_b - obj_a)
        expected = CustomList([5, 1, 3])
        comp_list(expected, obj_a)
        expected = CustomList([1, 2, 7])
        comp_list(expected, obj_b)

    def test_subtraction_with_smaller_cl(self):
        obj_a = CustomList([5, 1, 3, 7])
        obj_b = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4, 7])
        comp_list(expected, obj_a - obj_b)
        expected = CustomList([-4, 1, 4, -7])
        comp_list(expected, obj_b - obj_a)
        expected = CustomList([5, 1, 3, 7])
        comp_list(expected, obj_a)
        expected = CustomList([1, 2, 7])
        comp_list(expected, obj_b)

    def test_subtraction_with_longer_cl(self):
        obj_a = CustomList([1, 2, 7])
        obj_b = CustomList([5, 1, 3, 7])
        expected = CustomList([-4, 1, 4, -7])
        comp_list(expected, obj_a - obj_b)
        expected = CustomList([4, -1, -4, 7])
        comp_list(expected, obj_b - obj_a)
        expected = CustomList([1, 2, 7])
        comp_list(expected, obj_a)
        expected = CustomList([5, 1, 3, 7])
        comp_list(expected, obj_b)

    def test_addition_with_smaller_list(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = [2, 5]
        expected = CustomList([3, 7, 3, 4])
        comp_list(expected, obj_a + obj_b)
        comp_list(expected, obj_b + obj_a)
        expected = CustomList([1, 2, 3, 4])
        comp_list(expected, obj_a)
        expected = [2, 5]
        comp_list(expected, obj_b)

    def test_addition_with_longer_list(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = [2, 5, 7, 9, 6]
        expected = CustomList([3, 7, 10, 13, 6])
        comp_list(expected, obj_a + obj_b)
        comp_list(expected, obj_b + obj_a)
        expected = CustomList([1, 2, 3, 4])
        comp_list(expected, obj_a)
        expected = [2, 5, 7, 9, 6]
        comp_list(expected, obj_b)

    def test_subtraction_with_smaller_list(self):
        obj_a = CustomList([1, 2, 3, 4])
        obj_b = [2, 5]
        expected = CustomList([-1, -3, 3, 4])
        comp_list(expected, obj_a - obj_b)
        expected = CustomList([1, 3, -3, -4])
        comp_list(expected, obj_b - obj_a)
        expected = CustomList([1, 2, 3, 4])
        comp_list(expected, obj_a)
        expected = [2, 5]
        comp_list(expected, obj_b)

    def test_subtraction_with_longer_list(self):
        obj_a = CustomList([2, 5])
        obj_b = [1, 2, 3, 4]
        expected = CustomList([1, 3, -3, -4])
        comp_list(expected, obj_a - obj_b)
        expected = CustomList([-1, -3, 3, 4])
        comp_list(expected, obj_b - obj_a)
        expected = CustomList([2, 5])
        comp_list(expected, obj_a)
        expected = [1, 2, 3, 4]
        comp_list(expected, obj_b)

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
        comp_list(f"[1, 2, 3, 4], sum=10", str(obj_a))


if __name__ == '__main__':
    unittest.main()
