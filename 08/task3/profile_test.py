"""Demonstration of profile_deco"""
from profile_deco import profile_deco
import time


@profile_deco
def add(a, b):
    time.sleep(0.1)
    return a + b


for i in range(20):
    add(1, 2)

add.print_stat()
