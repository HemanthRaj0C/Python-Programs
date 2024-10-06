import multiprocessing
import time

# CPU-bound task: Sum of squares of numbers in a given range
def sum_of_squares(n):
    return sum(i * i for i in range(n))

# Sequential version of the task
def sequential_sum_of_squares(n, num_processes):
    total = 0
    for _ in range(num_processes):
        total += sum_of_squares(n)
    return total

# Parallel version of the task using multiprocessing
def parallel_sum_of_squares(n, num_processes):
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(sum_of_squares, [n] * num_processes)
    return sum(results)

if __name__ == "__main__":
    N = 10**6  # Range for calculating sum of squares
    num_processes = 4  # Number of processes to run in parallel

    # Sequential execution
    start_time = time.time()
    result_seq = sequential_sum_of_squares(N, num_processes)
    sequential_time = time.time() - start_time
    print(f"Sequential Result: {result_seq}")
    print(f"Sequential Time: {sequential_time:.4f} seconds\n")

    # Parallel execution
    start_time = time.time()
    result_par = parallel_sum_of_squares(N, num_processes)
    parallel_time = time.time() - start_time
    print(f"Parallel Result: {result_par}")
    print(f"Parallel Time: {parallel_time:.4f} seconds\n")

    # Compare performance
    print(f"Performance Improvement: {sequential_time / parallel_time:.2f}x")
