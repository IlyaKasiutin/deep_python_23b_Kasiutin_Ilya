"""Configuration of loggers"""

import logging


FILE_FORMATTER = logging.Formatter("%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
STREAM_FORMATTER = logging.Formatter(">>> %(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")


class CustomFilter(logging.Filter):
    """Filter implementation"""
    def filter(self, record):
        return 'key' in record.msg


def get_filters(args):
    filters = []
    if args.f:
        custom_filter = CustomFilter()
        filters.append(custom_filter)
    return filters


def get_file_handler(filename: str, mode='w'):
    handler = logging.FileHandler(filename, mode)
    handler.setFormatter(FILE_FORMATTER)
    return handler


def get_stream_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(STREAM_FORMATTER)
    return handler


def get_handlers(args):
    handlers = []
    file_handler = get_file_handler("cache.log")
    handlers.append(file_handler)

    if args.s:
        stream_handler = get_stream_handler()
        handlers.append(stream_handler)
    return handlers


def create_custom_logger(name: str, level: int):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger


def apply_filters_to_handlers(handlers: list[logging.Handler], filters: list[logging.Filter]):
    if not filters:
        return

    for handler in handlers:
        for f in filters:
            handler.addFilter(f)


def apply_handlers_to_logger(logger: logging.Logger, handlers: list[logging.Handler]):
    if not handlers:
        return

    for handler in handlers:
        logger.addHandler(handler)
