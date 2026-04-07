# Why to use Enumerate
# You're creating a tea menu board.
# Each item must be numbered

# Task:
# Use enumerate() to print menu items with numbers

menu = ["Masala Chai", "Adrak Chai", "Elaichi Chai", "Ginger Chai"]

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")