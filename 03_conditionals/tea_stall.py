# A tea stall offers different prices for different cup sizes.
# Write a program that calculate the price based on the sizes.
# Task:
# Input: "small", "medium". "large"
# Small-> ₹10, medium -> ₹15, large-> ₹20
# if invalid, shows: "Unknown cup size"

cup = input("Choose your cup size(small/medium/large):").lower()
if cup == 'small':
    print(f"Price is ₹10")
elif cup == "medium":
    print(f"Price is ₹15")
elif cup == "large":
    print(f"Price is ₹20")
else:
    print(f"Unknown cup size")