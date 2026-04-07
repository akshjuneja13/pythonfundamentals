# Python avoids confusion between assignment and comparison
# Using the walrus operator (:=) for inline assignment

# Example 1: Checking remainder
value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

# Example 2: Choosing a chai cup size
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")

# Example 3: Choosing a flavor
flavours = ["masala", "ginger", "lemon", "mint"]
print("Available flavours:", flavours)

while (flavour := input("Choose your flavor: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You chose {flavour} chai")  