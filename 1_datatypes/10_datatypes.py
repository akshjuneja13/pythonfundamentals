# Dictionary: collection of key-value pairs

# Creating a dictionary
chai_order = dict(type="Ginger chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

# Another way to create a dictionary
chai_recipe = {}

chai_recipe["base"] = "black tea"
chai_recipe["spice"] = "ginger"

print(f"Chai base: {chai_recipe['base']}")
print(f"Chai spice: {chai_recipe['spice']}")
print(f"Recipe details: {chai_recipe}")

# Deleting an item
del chai_recipe["spice"]
print(f"Chai recipe after deleting spice: {chai_recipe}")

# Membership test (check if key exists)
print(f"Is 'base' a key in chai recipe? {'base' in chai_recipe}")

# Dictionary methods
chai_order = {"type": "Ginger chai", "size": "medium", "sugar": 2}

print(f"Keys: {chai_order.keys()}")
print(f"Values: {chai_order.values()}")
print(f"Items: {chai_order.items()}")

# Remove last inserted item
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

# Update dictionary
extra_spices = {"cinnamon": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated recipe details: {chai_recipe}")

# Accessing values
chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")

# Using get() to avoid KeyError
customer_note = chai_order.get("customer_note", "No special requests")
print(f"Customer note: {customer_note}")