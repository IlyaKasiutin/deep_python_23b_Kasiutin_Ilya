import argparse
from lru_cache import LRUCache


parser = argparse.ArgumentParser('logger')
parser.add_argument('-s', action='store_true')
parser.add_argument('-f', action='store_true')


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")
cache.set("k3", "val3")



