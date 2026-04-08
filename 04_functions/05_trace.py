# Task:
# Use this function to calculate the bill for different orders


def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 5)
print(f"Total bill amount: {my_bill}")

print("Calculating bill for another order...")
another_bill = calculate_bill(2, 4)
print(f"Total bill amount: {another_bill}")