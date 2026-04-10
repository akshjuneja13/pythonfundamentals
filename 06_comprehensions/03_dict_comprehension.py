# Dictionary comprehension example

tea_prices_inr = {
    "Masala Chai": 40,
    "Elaichi Chai": 50,
    "Spicy Chai": 200
}

# Convert INR to USD (assuming 1 USD = 80 INR)
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)