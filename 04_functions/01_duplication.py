# Function - Reducing Duplication

# You are managing a busy tea stall.
# You receive many orders and want to print each customer's order.

# Task:
# Write a function print_order(name, chai_type)
# Call it multiple times for different customers

# Here we define the function with parameters
def print_order(name, chai_type):
    print(f"Serving {chai_type} to {name}")

# Here we pass arguments when calling the function
print_order("Alice", "Masala Chai")
print_order("Bob", "Ginger Chai")