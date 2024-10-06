# Example Program to Debug and Test
def is_even(n):
    """Returns True if n is even, else False (i.e., odd)."""
    return n % 2 == 0



# Using pdb for Debugging
import pdb

def is_even_debugged(n):
    """Returns True if n is even, else False (i.e., odd)."""
    pdb.set_trace()  # Start pdb debugger here
    return n % 2 == 0

# Testing pdb
if __name__ == "__main__":
    print(is_even_debugged(10))  # Set a breakpoint here to debug the code



# Using unittest Framework
import unittest

class TestEven(unittest.TestCase):

    def test_even(self):
        self.assertTrue(is_even(4))  # 4 is even
        self.assertFalse(is_even(7))  # 7 is odd

    def test_edge_cases(self):
        self.assertTrue(is_even(0))  # 0 is considered even
        self.assertTrue(is_even(-2))  # Negative even numbers should also return True
        self.assertFalse(is_even(-3))  # Negative odd numbers should return False

if __name__ == '__main__':
    unittest.main()



# Using pytest Framework
import pytest

def test_is_even():
    assert is_even(4) == True  # 4 is even
    assert is_even(7) == False  # 7 is odd

def test_edge_cases():
    assert is_even(0) == True  # 0 is even
    assert is_even(-2) == True  # Negative even number
    assert is_even(-3) == False  # Negative odd number

