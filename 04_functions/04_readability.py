# Task:
# Create a function add_vat(price, vat_rate)
# Use it to compute the final prices for three orders


def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100, 200, 300]

for price in orders:
    final_price = add_vat(price, 10)
    print(f"Original Price {price} Final price with VAT: {final_price}")