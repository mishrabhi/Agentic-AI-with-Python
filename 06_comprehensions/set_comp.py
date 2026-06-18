# Set comprehension
# Syntax: {expression for item in iterable if condition}

favourite_chais = [
    "Masala Chai",
    "Green tea",
    "Masala chai",
    "Lemon tea",
    "Green Tea",
    "Elaichi tea"
]

unique_chai = {chai for chai in favourite_chais if len(chai) < 8}
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)