"""Filter which check if 'key' in record message"""

import logging


class CustomFilter(logging.Filter):
    """Filter implementation"""
    def filter(self, record):
        return 'key' in record.msg
