# Building a chai price calculator using conditional
# A tea stall offers different prices for different cup sizes
# Write a program that calculates the price based on cup size

# Task:
# Input: "small", "medium", "large"
# small: $2, medium: $3, large: $4
# If invalid: show "Unknown cup size"

cup = input("Enter cup size (small, medium, large): ")

if cup == "small":
    price = 2
    print(f"Price for {cup} cup: ${price}")

elif cup == "medium":
    price = 3
    print(f"Price for {cup} cup: ${price}")

elif cup == "large":
    price = 4
    print(f"Price for {cup} cup: ${price}")

else:
    print("Unknown cup size")