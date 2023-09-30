import unittest
from unittest import mock
import json
import sys
sys.path.append('../src')
from json_parser import parse_json


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.js = {'name': 'Марфа Руслановна Рогова',
              'address': 'с. Суздаль, ул. Леваневского, д. 17 к. 9/4, 130479',
              'company': 'ООО «Котов»',
              'country': 'Сальвадор',
              'text': 'Собеседник плод социалистический неудобно палец затянуться.'}
        self.js = json.dumps(self.js)
        self.m = mock.MagicMock()

    def test_with_match(self):
        parse_json(self.js, ['name'], ['Марфа', 'Марфа'], self.m)
        parse_json(self.js, ['name', 'name'], ['МАРФА'], self.m)
        parse_json(self.js, ['name'], ['марфа'], self.m)

        self.assertEqual(3, self.m.call_count)
        expected_calls = [mock.call('Марфа')] * 3
        self.assertEqual(expected_calls, self.m.mock_calls)

    def test_without_match(self):
        parse_json(self.js, ['name'], ['Юлия'], self.m)
        parse_json(self.js, ['Имя'], ['Марфа'], self.m)
        self.assertEqual(0, self.m.call_count)

    def test_with_multiple_match(self):
        parse_json(self.js, ['name', 'country'], ['Марфа', 'Сальвадор'], self.m)
        self.assertEqual(2, self.m.call_count)
        expected_calls = [mock.call('Марфа'),
                          mock.call('Сальвадор')]
        self.assertEqual(expected_calls, self.m.mock_calls)

    def test_with_empty_required_fields(self):
        parse_json(self.js, [], ['Марфа'], self.m)
        self.assertEqual(0, self.m.call_count)

    def test_with_empty_keywords(self):
        parse_json(self.js, ['name'], [], self.m)
        self.assertEqual(0, self.m.call_count)

    def test_with_empty_json(self):
        self.js = "{}"
        parse_json(self.js, ['name'], ['Марфа'], self.m)
        self.assertEqual(0, self.m.call_count)

    def test_with_none_required_fields(self):
        with self.assertRaises(TypeError) as err:
            parse_json(self.js, keywords=['Марфа'], keyword_callback=self.m)

    def test_with_none_keywords(self):
        with self.assertRaises(TypeError) as err:
            parse_json(self.js, required_fields=['name'], keyword_callback=self.m)

    def test_with_none_callback(self):
        with self.assertRaises(TypeError) as err:
            parse_json(self.js, required_fields=['name'], keywords=['Марфа'])

    def test_with_wrong_type(self):
        with self.assertRaises(TypeError) as err:
            parse_json(self.js, 1, dict(), set())

    def test_with_wrong_json_type(self):
        with self.assertRaises(json.decoder.JSONDecodeError) as err:
            parse_json("", ['name'], ['Марфа'], self.m)

if __name__ == '__main__':
    unittest.main()
