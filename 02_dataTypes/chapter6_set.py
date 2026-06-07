# set

essential_spices = {'cardamom', 'ginger', 'cloves'}
optional_spice = {'cinnamon', "ginger", "black pepper"}

all_spices = essential_spices | optional_spice
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spice
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spice
print(f"Only in essential: {only_in_essential}")

# membership test
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")