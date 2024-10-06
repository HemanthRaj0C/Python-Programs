# Function to demonstrate unpacking of *args (positional arguments)
def args_example(*args):
    print("Positional arguments (*args):", args)
    for i, arg in enumerate(args):
        print(f"Argument {i+1}: {arg}")

# Function to demonstrate unpacking of **kwargs (keyword arguments)
def kwargs_example(**kwargs):
    print("Keyword arguments (**kwargs):", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Function that accepts both *args and **kwargs
def mixed_example(*args, **kwargs):
    print("\nMixed arguments (*args and **kwargs):")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Experimenting with *args
print("Calling args_example with multiple arguments:")
args_example(1, 2, 3, "Hello", True)

# Experimenting with **kwargs
print("\nCalling kwargs_example with keyword arguments:")
kwargs_example(a=10, b="World", c=3.14)

# Experimenting with mixed *args and **kwargs
print("\nCalling mixed_example with both positional and keyword arguments:")
mixed_example(1, 2, 3, x="foo", y="bar", z=42)

# Unpacking a list and dictionary into function calls
list_args = [10, 20, 30]
dict_kwargs = {"name": "Alice", "age": 25, "city": "Wonderland"}

print("\nUnpacking list and dictionary into mixed_example:")
mixed_example(*list_args, **dict_kwargs)