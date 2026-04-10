# Set comprehension example

favourite_chais = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Ginger Chai",
    "Green Tea",
    "Elaichi Chai"
]

# Get unique chai names with length > 10
unique_chai = {chai for chai in favourite_chais if len(chai) > 10}

print(unique_chai)


# Dictionary of recipes
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

# Get all unique spices from recipes
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)