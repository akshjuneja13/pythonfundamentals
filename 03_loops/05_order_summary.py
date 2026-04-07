# Zip can combine lists
# You are preparing an order summary with customer names and bills

# Task:
# Use two lists: one for names and one for bills
# Print: "[name] paid Rs [amount]"

names = ["Anu", "Amit", "Karan", "Sonal", "Divya"]
bills = [120, 250, 90, 300, 150]

for name, bill in zip(names, bills):
    print(f"{name} paid Rs {bill}")