# You are preparing a order summary with customer names and their total bill
# Task:
# Use two lists: one for names and one for bills
# Print: "[Name] paid ₹[amount]"

names = ["Abhishek", 'Meera', "Rinki"]
bills = [50, 100, 70]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")