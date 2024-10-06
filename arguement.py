# Positional Arguments
def positional_example(a, b):
    print("Positional Example a:", a, "b:", b)

# Keyword Arguments
def keyword_example(a, b):
    print("Keyword Example a:", a, "b:", b)

# Default Arguments
def default_example(a, b=10):
    print("Default Example a:", a, "b:", b)

# Variable Length Arguments (*args for non-keyword, **kwargs for keyword)
def variable_length_example(*args, **kwargs):
    print("Variable Length Example args:", args, "kwargs:", kwargs)

# Experimenting with Positional Arguments
print("Calling positional_example(1, 2):")
positional_example(1, 2)

# Experimenting with Keyword Arguments
print("\nCalling keyword_example(a=1, b=2):")
keyword_example(a=1, b=2)

print("Calling keyword_example(b=2, a=1):")
keyword_example(b=2, a=1)

# Experimenting with Default Arguments
print("\nCalling default_example(5):")
default_example(5)

print("Calling default_example(5, 15):")
default_example(5, 15)

# Experimenting with Variable-Length Arguments
print("\nCalling variable_length_example(1, 2, 3, x=10, y=20):")
variable_length_example(1, 2, 3, x=10, y=20)

print("Calling variable_length_example(x=10, y=20):")
variable_length_example(x=10, y=20)