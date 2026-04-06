# Initializing an empty set
spice_mix = set()

# Display the ID and contents of the initial spice mix
print(f"Initial spice mix ID: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")

# Adding spices to the set
spice_mix.add("cinnamon")
spice_mix.add("cardamom")  # Sets are mutable

# Display the updated spice mix
print(f"After adding spices: {spice_mix}")
print(f"Spice mix ID after adding spices: {id(spice_mix)}")