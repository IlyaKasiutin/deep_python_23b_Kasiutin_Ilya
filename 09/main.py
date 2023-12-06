"""Main file"""


from parsing_args import get_args
from lru_cache import LRUCache, logger
from logging_config import get_handlers, get_filters, apply_filters_to_handlers, apply_handlers_to_logger


if __name__ == "__main__":
    args = get_args()

    handlers = get_handlers(args)
    filters = get_filters(args)
    apply_filters_to_handlers(handlers, filters)
    apply_handlers_to_logger(logger, handlers)

    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.set("k3", "val3")
    cache.get("k1")
    cache.get("k2")
