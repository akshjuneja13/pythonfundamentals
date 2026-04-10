# Simple variable
chai = "Ginger chai"

# Function to prepare chai
def prepare_chai(order):
    return f"Preparing {order}"

# Calling the function
print(prepare_chai(chai))
# Output: Preparing Ginger chai


# Working with lists (mutable objects)
chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42  # Fix: assignment operator

edit_chai(chai)
print(chai)
# Output: [1, 42, 3]


# Function with parameters
def make_chai(tea, milk, sugar):
    print(f"Making chai with {tea} tea, {milk} milk and {sugar} sugar")

# Positional arguments
make_chai("Ginger", "Full Cream", "2 spoons")

# Keyword arguments
make_chai(tea="Green", milk="Skimmed", sugar="1 spoon")


# *args and **kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Cinnamon", "Cardamom", sweetener="Honey", foam="yes")


# Default argument example
def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order(["Masala chai", "Green chai"])