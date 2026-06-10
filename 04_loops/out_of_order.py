# Some chai flavours are out of stock
# You want to skip those and stop entirely if someone requests a restricted flavour
# Task:
# Skip if flavour is Out of Stock
# Break if flavour is Discontinued

flavours = ['ginger', 'out of stock', 'lemon', 'discontinued', 'tulsi']

for flavour in flavours:
    if flavour == 'out of stock' :
        continue  
    if flavour == 'discontinued':
        break
    print(f"{flavour} item found!")
print(f"Out side of loop")