# Generator comprehension
# Syntax: (expression for item in iterable if condition)

daily_sales = [5,10,12,8,15,4]
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)