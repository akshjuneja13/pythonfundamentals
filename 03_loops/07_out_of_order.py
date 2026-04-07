# Handling restricted tea flavors
# Task:
# Skip if flavor is "Out of Stock"
# Break if flavor is "Discontinued"

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued"]

for flavor in flavours:
    if flavor == "Out of Stock":
        print(f"Sorry, {flavor} is currently unavailable.")
        continue
    elif flavor == "Discontinued":
        print(f"Sorry, {flavor} has been discontinued.")
        break
    else:
        print(f"Preparing your {flavor} chai!")

print("Thank you for visiting our tea stall!")