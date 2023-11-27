import unittest
import cjson
import json


class TestJsonDumps(unittest.TestCase):
    def test_cjson_vs_json_dumps(self):
        json_dict = {"hello": 10, "world": "value"}
        json_doc = json.dumps(json_dict)
        cjson_doc = cjson.dumps(json_dict)
        self.assertEqual(json_doc, cjson_doc)
    
    def test_cjson_json_dumps_loads(self):
        json_dict = {"hello": 10, "world": "value"}
        self.assertEqual(json_dict, cjson.loads(cjson.dumps(json_dict)))

    def test_dict_unchanged(self):
        json_dict = {"hello": 10, "world": "value"}
        cjson.dumps(json_dict)
        self.assertEqual({"hello": 10, "world": "value"}, json_dict)

    def test_incorrect_value(self):
        json_dict1 = {"hello": [10, 20], "world": "value"}
        json_dict2 = {"hello": 10, "world": ["value"]}
        with self.assertRaises(TypeError):
            cjson.dumps(json_dict1)
            cjson.dumps(json_dict2)

    def test_incorrect_key(self):
        json_dict = {10: "hello", "world": "value"}
        with self.assertRaises(TypeError):
            cjson.dumps(json_dict)

    def test_incorrect_input_value(self):
        json_str = '{"hello": 10, "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.dumps(json_str)


if __name__ == "__main__":
    unittest.main()    
