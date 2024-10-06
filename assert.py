# Function to validate account balance
def withdraw(balance, amount):
    # Assert that the balance is non-negative
    assert balance >= 0, "Balance cannot be negative."
    
    # Assert that the amount to withdraw is greater than zero
    assert amount > 0, "Withdrawal amount must be greater than zero."
    
    # Assert that there are sufficient funds
    assert balance >= amount, "Insufficient funds."
    
    balance -= amount
    print(f"Withdrawal successful! New balance: ${balance}")
    return balance

# Function to validate a list of items
def validate_items(items):
    # Assert that items is a non-empty list
    assert isinstance(items, list), "Items should be a list."
    assert len(items) > 0, "List of items should not be empty."
    
    # Assert that all items in the list are strings and not empty
    for item in items:
        assert isinstance(item, str) and len(item) > 0, f"Item '{item}' is not valid."
    
    print(f"All {len(items)} items are valid.")
    return True

# Testing the custom assertions
try:
    # Valid withdraw
    balance = 100
    print("Trying to withdraw $30:")
    new_balance = withdraw(balance, 30)
    
    # Invalid withdraw: amount greater than balance
    print("\nTrying to withdraw $200:")
    withdraw(new_balance, 200)  # AssertionError will be raised here

except AssertionError as error:
    print(f"AssertionError: {error}")

try:
    # Valid items list
    print("\nValidating items list:")
    validate_items(["apple", "banana", "cherry"])
    
    # Invalid case: empty string in items
    print("\nValidating items list with an empty string:")
    validate_items(["apple", "", "cherry"])  # AssertionError will be raised here

except AssertionError as error:
    print(f"AssertionError: {error}")
