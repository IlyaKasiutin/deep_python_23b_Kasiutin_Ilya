import unittest
from lru_cache import LRUCache


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual("val1", cache.get("k1"))
        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual(None, cache.get("k3"))

    def test_order(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual("val3", cache.get("k3"))
        self.assertEqual(None, cache.get("k1"))

    def test_update_order(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual("k1", cache.order[0])
        self.assertEqual("k2", cache.order[1])

        cache.get("k1")
        self.assertEqual("k2", cache.order[0])
        self.assertEqual("k1", cache.order[-1])


if __name__ == '__main__':
    unittest.main()
