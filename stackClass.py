import timeit
from collections import deque

# Custom Stack class implemented using a list
class CustomStack:
    def __init__(self):
        self.stack = []
    
    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)
    
    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Test performance of custom stack, list, and deque for stack-like behavior
def custom_stack_test(custom_stack, n):
    for i in range(n):
        custom_stack.push(i)
    while not custom_stack.is_empty():
        custom_stack.pop()

def list_stack_test(stack_list, n):
    for i in range(n):
        stack_list.append(i)
    while stack_list:
        stack_list.pop()

def deque_stack_test(stack_deque, n):
    for i in range(n):
        stack_deque.append(i)
    while stack_deque:
        stack_deque.pop()

# Performance comparison
if __name__ == "__main__":
    n = 100000  # Number of operations

    # Custom Stack
    custom_stack = CustomStack()
    custom_stack_time = timeit.timeit(lambda: custom_stack_test(custom_stack, n), number=1)
    print(f"Custom Stack Time: {custom_stack_time:.6f} seconds")

    # Python List
    stack_list = []
    list_time = timeit.timeit(lambda: list_stack_test(stack_list, n), number=1)
    print(f"Python List Time: {list_time:.6f} seconds")

    # Deque from collections
    stack_deque = deque()
    deque_time = timeit.timeit(lambda: deque_stack_test(stack_deque, n), number=1)
    print(f"Python Deque Time: {deque_time:.6f} seconds")
