"""Main file"""


import argparse
import logging
from lru_cache import LRUCache, logger, handler
from filter import CustomFilter


parser = argparse.ArgumentParser('logger')
parser.add_argument('-s', action='store_true')
parser.add_argument('-f', action='store_true')
args = parser.parse_args()

if args.s:
    stream_handler = logging.StreamHandler()
    if args.f:
        custom_filter = CustomFilter()
        handler.addFilter(custom_filter)
        stream_handler.addFilter(custom_filter)
    formatter = logging.Formatter(">>> %(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.set("k3", "val3")
    cache.get("k1")
    cache.get("k2")
