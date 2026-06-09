# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosas,it confirms the order. Otherwise it says not available. 
# Task:
# Take snack input
# If its cookies or samosas, confirm the order 
# Else, show unavailability

snack = input("Enter your preferred snack: ").lower()
print(f"User asked: {snack}")
if snack == "cookies" or  snack == "samosa":
    print(f"Great choice! We will serve your {snack} soon.")
else:
    print(f"Sorry! We only serve cookies or samosa.")
