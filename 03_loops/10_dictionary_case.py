# Dictionary in place of match-case for coupon discounts

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F20"},
    {"id": 3, "total": 80, "coupon": "P20"}
]

# Discount mapping: coupon -> (percent discount, fixed discount)
discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    final_amount = user["total"] * (1 - percent) - fixed  # apply discount
    print(f"User {user['id']} paid Rs {final_amount}")