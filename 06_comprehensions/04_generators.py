# Generator expressions

# (expression for item in iterable if condition)
# Uses less memory compared to list comprehension

daily_sales = [5, 10, 12, 7, 2, 3, 8, 9, 15]

# Total sales using generator expression
total_sales = sum(sale for sale in daily_sales if sale > 5)

print(total_sales)


# Total cups sold greater than 5 (list comprehension)
total_cups = [sale for sale in daily_sales if sale > 5]

print(total_cups)