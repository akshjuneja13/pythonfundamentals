# Take snack input
# If it is cookie or brownie, confirm the order
# Otherwise, say it is not available

snack = input("What snack would you like to order? ")

if snack == "cookie" or snack == "brownie":
    print("Order confirmed!")
else:
    print("Sorry, that snack is not available.")