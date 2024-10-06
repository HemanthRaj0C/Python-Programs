import time
import tracemalloc

# Function to measure time and memory usage
def measure_performance(func, *args):
    start_time = time.time()
    tracemalloc.start()

    func(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time: {end_time - start_time:.6f} seconds, Memory: {peak / 1024:.2f} KB")

# Write and Read Text File
def write_text_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def read_text_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# Write and Read Binary File
def write_binary_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def read_binary_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

# Testing the performance
if __name__ == "__main__":
    text_data = "Hello World! " * 100000  # Large amount of text
    binary_data = text_data.encode()  # Convert text to binary

    print("Text File Write:")
    measure_performance(write_text_file, 'textfile.txt', text_data)

    print("Text File Read:")
    measure_performance(read_text_file, 'textfile.txt')

    print("\nBinary File Write:")
    measure_performance(write_binary_file, 'binaryfile.bin', binary_data)

    print("Binary File Read:")
    measure_performance(read_binary_file, 'binaryfile.bin')
