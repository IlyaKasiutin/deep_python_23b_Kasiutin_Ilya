"""Main file"""


import argparse
from lru_cache import LRUCache, logger
from logging_config import CustomFilter, get_file_handler, get_stream_handler


parser = argparse.ArgumentParser('logger')
parser.add_argument('-s', action='store_true')
parser.add_argument('-f', action='store_true')
args = parser.parse_args()


file_handler = get_file_handler("cache.log")
handlers = [file_handler]
logger.addHandler(file_handler)

if args.s:
    stream_handler = get_stream_handler()
    handlers.append(stream_handler)


if args.f:
    custom_filter = CustomFilter()
    for handler in handlers:
        handler.addFilter(custom_filter)

for handler in handlers:
    logger.addHandler(handler)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.set("k3", "val3")
    cache.get("k1")
    cache.get("k2")
