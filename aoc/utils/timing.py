import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time of ({func.__name__}): {execution_time:.2f} milliseconds")
        return result
    return wrapper
