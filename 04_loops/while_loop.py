# You want to simulate tea heating
# It starts at 40 degree celcius and boils at 100
# Task:
# Use a while loop
# Increase temperature by 15 until it reaches or exceeds 100
# Print each temperature setup

temperature = 40
while temperature < 100:
    print(f"Current temperature: {temperature}")
    temperature += 15
print(f"Tea is ready to boil!")
