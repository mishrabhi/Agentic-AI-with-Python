# Return 

# Nothing -> Implicitly returns none


def make_chai():
    return "Abhishek, here is your masala chai"

# print(make_chai())
return_value = make_chai()
print(return_value)

# Returning nothing
def idle_chaiwala():
    pass
print(idle_chaiwala()) #none

# return one 
def sold_cups():
    return 120
total = sold_cups()
print(total)


# return early from a function
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry! Chai over"
    return "Chai is ready"
print(chai_status(0))
print(chai_status(5))

# returing multiple values
def chai_report():
    return 100, 20 #sold, remaining
sold, remianing = chai_report()
print("sold", sold)
print("remaining", remianing)