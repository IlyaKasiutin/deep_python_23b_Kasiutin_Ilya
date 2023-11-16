"""Profile decorator"""
import cProfile
from typing import Callable


class ProfiledFunc:
    def __init__(self, func: Callable, profiler_stats: cProfile.Profile):
        self.func = func
        self.profiler_stats = profiler_stats

    def print_stat(self):
        print(f"Stats for {self.func.__name__}")
        print('-' * 50)
        self.profiler_stats.print_stats(sort='ncalls')
        print('-' * 50)


def profile_deco(func):
    profiler = cProfile.Profile()
    profiled_function = ProfiledFunc(func, profiler)

    def wrapper(*args, **kwargs):
        profiler.enable()
        res = profiler.runcall(func, *args, **kwargs)
        profiler.disable()
        return res

    wrapper.print_stat = profiled_function.print_stat

    return wrapper
