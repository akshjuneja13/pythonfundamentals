# Function that returns a value
def make_chai():
    return "Here is your masala chai"

return_value = make_chai()
print(return_value)


# Function with no return (returns None)
def idle_chaiwala():
    pass

print(idle_chaiwala())


# Function returning a number
def sold_cups():
    return 120

total = sold_cups()
print(total)


# Conditional function
def chai_status(cups_left):
    if cups_left <= 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))


# Function returning multiple values
def chai_report():
    return 100, 20  # sold, remaining

sold, remaining = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)