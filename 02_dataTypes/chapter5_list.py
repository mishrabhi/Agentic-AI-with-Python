# list

ingredients = ['water', 'milk', 'black tea']
ingredients.append('sugar')
print(f"Ingredients are: {ingredients}")
ingredients.remove('water');
print(f"Ingredients are: {ingredients}")

spice_options = ['ginger', 'cardamom']
chai_ingredients = ['water', 'milk']
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea");
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"last_added: {last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"reversed: {chai_ingredients}")

chai_ingredients.sort()
print(f"sorted: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"maximum: {max(sugar_levels)}")
print(f"minimum: {min(sugar_levels)}")


# operator overloading
base_liquid = ['water', 'milk']
extra_flavour = ['ginger']
full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ['black tea'] * 3
print(f"Strong brew: {strong_brew}")

strong_brew = ['black tea', 'water'] * 3
print(f"Strong brew: {strong_brew}")
