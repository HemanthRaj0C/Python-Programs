import pdb

# Global variable
x = "global variable"

def outer_function():
    # Local variable in outer_function
    x = "outer function variable"
    
    def inner_function():
        nonlocal x  # Refers to the variable in the nearest enclosing scope (outer_function)
        pdb.set_trace()  # Set a breakpoint to inspect the local and nonlocal variables
        print("Before modification in inner_function:", x)
        x = "modified by inner_function"
        print("After modification in inner_function:", x)
    
    print("Before calling inner_function:", x)
    inner_function()
    print("After calling inner_function:", x)

def global_modifier():
    global x  # Refers to the global variable x
    pdb.set_trace()  # Set a breakpoint to inspect the global variable
    print("Before modification in global_modifier:", x)
    x = "modified by global_modifier"
    print("After modification in global_modifier:", x)

# Demonstrate the scopes
print("Initial global variable:", x)
pdb.set_trace()  # Set a breakpoint before calling the outer function
outer_function()
print("Global variable after calling outer_function:", x)

pdb.set_trace()  # Set a breakpoint before modifying the global variable
global_modifier()
print("Global variable after calling global_modifier:", x)
