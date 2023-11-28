"""Profile decorator"""
import cProfile


def profile_deco(func):
    """Function calls profiling decorator"""
    profiler = cProfile.Profile()

    def wrapper(*args, **kwargs):
        profiler.enable()
        res = profiler.runcall(func, *args, **kwargs)
        profiler.disable()
        return res

    wrapper.print_stat = profiler.print_stats

    return wrapper
