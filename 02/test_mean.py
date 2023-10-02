import unittest
from unittest import mock
from mean import mean
import time
import sys
from io import StringIO
from contextlib import redirect_stdout


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.func = mock.Mock()

    def test_calls_count(self):
        @mean(10)
        def foo(func, *args):
            func(*args)

        for i in range(20):
            foo(self.func, 'test string', 12.5)

        self.assertEqual(20, self.func.call_count)

    def test_calls_arguments(self):
        @mean(10)
        def foo(func, *args):
            func(*args)

        for i in range(5):
            foo(self.func, 'test string', 12.5)
        expected_calls = [mock.call('test string', 12.5)] * 5
        self.assertEqual(expected_calls, self.func.mock_calls)

    def test_calculated_value(self):
        @mean(10)
        def timer():
            time.sleep(0.2)

        with StringIO() as buf, redirect_stdout(buf):
            for i in range(10):
                timer()
            output = buf.getvalue()
            output = float(output.split()[-1])
            eps = 10e-2
            self.assertLess(abs(0.2 - output), eps)

    def test_return_value(self):
        @mean(10)
        def add(a, b):
            return a + b

        res = add(1, 2)
        self.assertEqual(3, res)

    def test_with_wrong_argument(self):
        with self.assertRaises(TypeError):
            @mean('10')
            def foo():
                pass

            foo()


if __name__ == '__main__':
    unittest.main()
