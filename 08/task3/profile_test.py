"""Demonstration of profile_deco"""
import time
from profile_deco import profile_deco


@profile_deco
def add(a, b):
    """Demo function"""
    time.sleep(0.1)
    return a + b


for i in range(20):
    add(1, 2)

add.print_stat()
