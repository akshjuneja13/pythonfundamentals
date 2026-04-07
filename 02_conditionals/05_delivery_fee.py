# Delivery fees waiver system
# You run an online tea store.
# If the order amount is more than Rs 300, delivery is free
# otherwise it costs Rs 30.

# Task:
# Input: order_amount
# Use ternary operator to decide delivery fee

order_amount = float(input("Enter order amount: "))

delivery_fee = 0 if order_amount > 300 else 30

print(f"Delivery fee: Rs {delivery_fee}")