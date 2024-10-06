import timeit

# Class with direct access to attributes
class DirectAccess:
    def __init__(self, value):
        self.value = value

# Class using getter and setter methods
class GetterSetterAccess:
    def __init__(self, value):
        self._value = value  # Protected attribute to be accessed via getter and setter

    # Getter method
    @property
    def value(self):
        return self._value

    # Setter method
    @value.setter
    def value(self, new_value):
        self._value = new_value

# Function to test direct attribute access
def direct_access_test(obj, new_value):
    obj.value = new_value
    return obj.value

# Function to test getter and setter methods
def getter_setter_access_test(obj, new_value):
    obj.value = new_value  # Calls the setter method
    return obj.value  # Calls the getter method

# Main function to compare the performance
if __name__ == "__main__":
    direct_obj = DirectAccess(0)
    getter_setter_obj = GetterSetterAccess(0)

    # Measuring performance of direct access
    direct_time = timeit.timeit(lambda: direct_access_test(direct_obj, 10), number=1000000)

    # Measuring performance of getter and setter access
    getter_setter_time = timeit.timeit(lambda: getter_setter_access_test(getter_setter_obj, 10), number=1000000)

    # Printing the results
    print(f"Direct Access Time: {direct_time:.6f} seconds")
    print(f"Getter/Setter Access Time: {getter_setter_time:.6f} seconds")
