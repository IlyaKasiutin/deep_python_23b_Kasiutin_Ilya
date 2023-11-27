import unittest
import cjson
import json


class TestJsonLoads(unittest.TestCase):
    def test_cjson_vs_json_loads(self):
        json_str = '{"hello": 10, "world": "value"}'
        json_doc = json.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)
    
    def test_cjson_json_loads_dumps(self):
        json_str = '{"hello": 10, "world": "value"}'
        self.assertEqual(json_str, cjson.dumps(cjson.loads(json_str)))

    def test_str_unchanged(self):
        json_str = '{"hello": 10, "world": "value"}'
        cjson.loads(json_str)
        self.assertEqual('{"hello": 10, "world": "value"}', json_str)

    def test_incorrect_value(self):
        json_str1 = '{"hello": [10, 20], "world": "value"}'
        json_str2 = '{"hello": 10, "world": ["value"]}'
        json_str3 = '{"hello": 10abc, "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.loads(json_str1)
            cjson.loads(json_str2)
            cjson.loads(json_str3)

    def test_incorrect_key(self):
        json_str = '{10: "hello", "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.loads(json_str)

    def test_incorrect_input_value(self):
        json_dict = {"hello": 10, "world": "value"}
        with self.assertRaises(TypeError):
            cjson.loads(json_dict)


if __name__ == "__main__":
    unittest.main()    
