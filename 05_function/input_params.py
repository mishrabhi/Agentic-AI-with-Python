# Input Params

# chai = "Ginger chai"
# def prepare_chai(order):
#     print(f"Preparing", order)
# prepare_chai(chai)
# print(chai)

chai = [1,2,3]
def edit_chai(cup):
    cup[1] = 41
edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="low", milk="yes") #keywords

# Agrs and kwargs
# def special_chai(*args, **kwargs)
def special_chai(*ingredients, **extras):
    print(f"Ingredients", ingredients)
    print(f"Extras", extras)
special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")


def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order() # ["Masala"]
chai_order() #["Masala", "Masala"]
