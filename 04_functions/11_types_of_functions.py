# Pure function
def pure_chai(cups):
    return cups * 10


# Impure function (uses global variable)
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups * 10


# Recursive function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All chai are poured"
    return pour_chai(n - 1)

print(pour_chai(5))


# Lambda is an anonymous function
# Syntax: lambda arguments: expression

x = lambda a: a + 10
print(x(5))   # Output: 15

y = lambda a, b: a + b
print(y(5, 6))   # Output: 11


# Adding 10 to each element in a list
a = [1, 2, 3, 4]

for i in range(len(a)):
    a[i] = a[i] + 10

print(a)   # Output: [11, 12, 13, 14]


# Lambda with filter
chai_types = ["Masala", "Ginger", "Lemon"]

strong_chai = list(filter(lambda chai: chai != "Lemon", chai_types))

print(strong_chai)   # Output: ['Masala', 'Ginger']