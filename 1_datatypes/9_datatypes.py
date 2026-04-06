# Set and frozenset in Python
# A set is an unordered collection of unique elements.
# A frozenset is an immutable version of a set.

espresso_ingredients = {"coffee", "water", "coffee"}
print(f"Espresso ingredients: {espresso_ingredients}")

# Sets automatically remove duplicates ("coffee" appears only once)

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"clove", "ginger", "black pepper"}

# Union of sets
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# Intersection of sets
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Difference of sets
only_essential = essential_spices - optional_spices
print(f"Only essential spices: {only_essential}")

# Membership test
print(f"Is 'clove' an essential spice? {'clove' in essential_spices}")
print(f"Is 'clove' an optional spice? {'clove' in optional_spices}")

# Frozenset (immutable set)
frozen_essential_spices = frozenset(essential_spices)
print(f"Frozen essential spices: {frozen_essential_spices}")