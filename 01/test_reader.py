import unittest
from unittest import mock
from file_reader import file_reader


class MyReader(unittest.TestCase):
    def test_one_line_file(self):
        text = """
А роза упала на лапу Азора
        """
        test_file = mock.mock_open(read_data=text)
        with mock.patch('builtins.open', test_file, create=True) as mock_file:
            gen = file_reader("test", ["роза"])
            lst = list(gen)
            self.assertEqual(["А роза упала на лапу Азора"],lst)

    def test_multiple_line_file(self):
        text = """
А роза упала на лапу Азора
Роза
розы
        """
        test_file = mock.mock_open(read_data=text)
        with mock.patch('builtins.open', test_file, create=True) as mock_file:
            gen = file_reader("test", ["роза"])
            lst = list(gen)
            self.assertEqual(["А роза упала на лапу Азора", "Роза"], lst)

    def test_empty_answer(self):
        text = """Roses"""
        test_file = mock.mock_open(read_data=text)
        with mock.patch('builtins.open', test_file, create=True) as mock_file:
            gen = file_reader("test", ["роза"])
            lst = list(gen)
            self.assertEqual([], lst)

    def test_big_file(self):
        gen1 = list(file_reader('alice_in_wonderland.txt', ['alice']))
        gen2 = list(file_reader('alice_in_wonderland.txt', ['ALICE']))
        self.assertGreater(len(gen1), 0)
        self.assertEqual(list(gen1), list(gen2))

    def test_big_textio(self):
        with open('alice_in_wonderland.txt') as file:
            gen1 = list(file_reader(file, ['alice']))
            file.seek(0)
            gen2 = list(file_reader(file, ['ALICE']))
            self.assertGreater(len(gen1), 0)
            self.assertEqual(list(gen1), list(gen2))

    def test_multiple_words(self):
        text = """
Первая строка
Вторая строка
Третья строка
                """
        test_file = mock.mock_open(read_data=text)
        with mock.patch('builtins.open', test_file, create=True) as mock_file:
            gen = file_reader("test", ["первая", "вторая"])
            lst = list(gen)
            self.assertEqual(["Первая строка", "Вторая строка"], lst)

    def test_multiple_filters_in_one_string(self):
        text = """Первая строка текста
Вторая строка
Третья строка"""
        test_file = mock.mock_open(read_data=text)
        with mock.patch('builtins.open', test_file, create=True) as mock_file:
            gen = file_reader("test", ["первая", "вторая", "текста"])
            lst = list(gen)
            self.assertEqual(["Первая строка текста", "Вторая строка"], lst)


if __name__ == '__main__':
    unittest.main()
