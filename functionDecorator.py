#WITHOUT 
import time
import tracemalloc

def slow_function():
    total = 0
    for i in range(10**6):
        total += i
    return total

# Performance measurement without decorator
start_time = time.time()
tracemalloc.start()

slow_function()

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Without Decorator - Time: {end_time - start_time:.6f} seconds, Memory: {peak / 1024:.2f} KB")

#WITH
# Decorator to measure execution time and memory usage
def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        tracemalloc.start()

        result = func(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"With Decorator - Time: {end_time - start_time:.6f} seconds, Memory: {peak / 1024:.2f} KB")
        return result
    return wrapper

@performance_decorator
def slow_function_with_decorator():
    total = 0
    for i in range(10**6):
        total += i
    return total

# Performance measurement with decorator
slow_function_with_decorator()
