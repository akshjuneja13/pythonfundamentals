# List comprehension examples

menu = ["Masala Chai", "Ginger Chai", "Lemon Chai", "Elaichi Chai", "Iced Tea"]

# Get only iced tea items
iced_tea = [tea for tea in menu if "Iced" in tea]

# Get tea names with length greater than 10
iced_tea_new = [tea for tea in menu if len(tea) > 10]

print(iced_tea)
print(iced_tea_new)