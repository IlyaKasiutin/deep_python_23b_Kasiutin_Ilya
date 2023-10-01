import time


def mean(n):
    def inner_mean(func):
        launches = 0
        times_list = []

        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()

            nonlocal launches
            launches += 1

            execution_time = end_time - start_time

            if launches > n:
                times_list.pop(0)
            times_list.append(execution_time)

            print(f"Mean execution time= %.3f" % (sum(times_list) / len(times_list)))
            return res

        return inner

    return inner_mean
