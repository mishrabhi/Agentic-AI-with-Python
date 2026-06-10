staff = [("Amit", 16), ("Zara", 15), ('Raj', 17)]
for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff!")
        break
else:
    print(f"No one is eligible!")
