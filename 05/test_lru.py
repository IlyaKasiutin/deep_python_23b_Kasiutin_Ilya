import unittest
from lru_cache import LRUCache


class MyTestCase(unittest.TestCase):
    def test_base(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(None, cache.get("k3"))
        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))

        cache.set("k3", "val3")

        self.assertEqual("val3", cache.get("k3"))
        self.assertEqual(None, cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))

    def test_update_order(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual("k2", cache.head.key)
        self.assertEqual("k1", cache.tail.key)

        cache.get("k1")
        self.assertEqual("k1", cache.head.key)
        self.assertEqual("k2", cache.tail.key)

    def test_minimal_limit(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual(None, cache.get("k1"))

        # проверка, что кэш не изменился
        self.assertEqual("val2", cache.get("k2"))

    def test_change_value(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "new_val")
        cache.set("k3", "val3")  # нужно для проверки правильности вытеснения

        self.assertEqual("new_val", cache.get("k1"))
        self.assertEqual(None, cache.get("k2"))  # проверка, что вытеснился именно k2


if __name__ == '__main__':
    unittest.main()
