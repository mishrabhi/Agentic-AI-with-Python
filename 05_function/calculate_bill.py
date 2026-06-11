# You sell different chai sizes
# Instead of writing formula everywhere, create a funcion
# Task:
# Write calculate_bills(cups, price_per_cup)
# Return total bill
# Use this function for multiple orders

def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bills(3, 15)
print(f"Total bill is {my_bill}")
print(f"Order for table 2:", calculate_bills(2, 100))