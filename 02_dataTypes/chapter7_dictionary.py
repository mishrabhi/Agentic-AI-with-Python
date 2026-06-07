# dictionary

chai_order = dict(type="Masala chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = 'black_tea'
chai_recipe["liquid"] = 'milk'
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

del chai_recipe['liquid']
print(f"Recipe: {chai_recipe}")


chai_order = {"type" : "Ginger chai", "size" :" Medium", "sugar" : 1}
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f'Remove last items: {last_item}')

extra_spices = {"cardamom": "crushed", 'ginger': "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get('Note', "No Note")
print(f"Customer Note: {customer_note}")