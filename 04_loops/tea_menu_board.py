# You are creating tea menu board
# Each item must be numbered
# Task:
# Use enumerate() to print menu items with numbers

menu = ['green tea', 'lemon tea', 'spiced tea', 'mint tea']

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} ")