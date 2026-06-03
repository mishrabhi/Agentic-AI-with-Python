import sys

# Integer 

# Addition
black_tea_grams = 14
ginger_team_grams = 10
total_grams = black_tea_grams + ginger_team_grams
print(f"Total grams of base tea is: {total_grams}")

# Substraction
remaining_tea = black_tea_grams - ginger_team_grams
print(f"Total grams of remaining tea is: {remaining_tea}")

# Division
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is: {milk_per_serving}")

# Division(without decimal)
total_tea_bag = 7
pots = 4
bags_per_pot = total_tea_bag // pots
print(f"Whole tea bags per pot is: {bags_per_pot}")

# Modulus
total_cardamom_pots = 10
pots_per_cup = 3
left_pver_pots = total_tea_bag % pots_per_cup
print(f"Leftover c pots is: {left_pver_pots}")

# Power: 2*2*2
base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour strength is: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves: {total_tea_leaves_harvested}")

# boolean
is_boiling = True 
stri_count = 5
#  true is also denoted at 1 and false as 0
total_casting = is_boiling + stri_count  #upcasting
print(f"total_casting is: {total_casting}") #6

milk_present = 0 # no milk
print(f"Is there milk? {(bool(milk_present))}") #false

# logical operation
water_hot = True
tea_added = True
can_serve = water_hot + tea_added

print(f"Can serve chai? {can_serve}")


ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"ideal temp: {ideal_temp}");
print(f"current temp: {current_temp}");
print(f"difference is: {ideal_temp - current_temp}")
print(sys.float_info)