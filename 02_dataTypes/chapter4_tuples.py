# Tuples => ()
# Tuples are immutable

masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"ginger ratio is: {ginger_ratio}, cardamom ratio is : {cardamom_ratio}") 
# swap the ratio
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"ginger ratio is: {ginger_ratio}, cardamom ratio is : {cardamom_ratio}") 

# membership
print(f"Is ginger in masala spices? {'ginger' in masala_spices}") #false
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}") #true 


