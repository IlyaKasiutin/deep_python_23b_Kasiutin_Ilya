"""Filter which check if 'key' in record message"""

import logging


FILE_FORMATTER = logging.Formatter("%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
STREAM_FORMATTER = logging.Formatter(">>> %(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")


class CustomFilter(logging.Filter):
    """Filter implementation"""
    def filter(self, record):
        return 'key' in record.msg


def get_file_handler(filename: str, mode='w'):
    handler = logging.FileHandler(filename, mode)
    handler.setFormatter(FILE_FORMATTER)
    return handler


def get_stream_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(STREAM_FORMATTER)
    return handler


def create_custom_logger(name: str, level: int):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
