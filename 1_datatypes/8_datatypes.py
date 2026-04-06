# Basic list operations
ingredients = ["water", "milk", "black tea"]

ingredients.append("ginger")
print(f"Ingredients: {ingredients}")

ingredients.remove("milk")
print(f"Ingredients after removing milk: {ingredients}")

# Spice options
spice_options = ["ginger", "cardamom"]

# Chai ingredients
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients after inserting black tea: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last added ingredient: {last_added}")
print(f"Chai ingredients after popping last added ingredient: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai ingredients after reversing: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai ingredients after sorting: {chai_ingredients}")

# Sugar levels
sugar_levels = [3, 1, 2, 4, 5]

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
print(f"Total sugar levels: {sum(sugar_levels)}")

# Operator overloading (list concatenation)
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Full liquid mix: {full_liquid_mix}")