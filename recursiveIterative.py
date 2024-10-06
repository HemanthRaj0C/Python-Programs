import time

# Recursive version of Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative version of Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Function to measure execution time
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

# Testing with different input sizes
input_sizes = [10, 20, 30, 35]  # Adjust this for larger or smaller inputs
print("Comparing Recursive and Iterative Fibonacci")

for n in input_sizes:
    print(f"\nFibonacci({n}):")
    
    # Measuring recursive approach
    try:
        fib_rec, time_rec = measure_time(fibonacci_recursive, n)
        print(f"Recursive: Result = {fib_rec}, Time = {time_rec:.6f} seconds")
    except RecursionError:
        print(f"Recursive: RecursionError occurred for input size {n}")

    # Measuring iterative approach
    fib_iter, time_iter = measure_time(fibonacci_iterative, n)
    print(f"Iterative: Result = {fib_iter}, Time = {time_iter:.6f} seconds")
