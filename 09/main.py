import argparse
import logging
from lru_cache import LRUCache, logger


parser = argparse.ArgumentParser('logger')
parser.add_argument('-s', action='store_true')
parser.add_argument('-f', action='store_true')
args = parser.parse_args()

if args.s:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("stdout %(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")
cache.set("k3", "val3")
cache.get("k1")
cache.get("k2")
