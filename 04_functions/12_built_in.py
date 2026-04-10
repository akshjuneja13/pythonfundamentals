def chai_flavor(flavour="Masala"):
    """Return the flavor of chai."""
    return flavour


# Double underscore (dunder) attributes
print(chai_flavor.__doc__)   # This will print the docstring
print(chai_flavor.__name__)  # This will print the function name

help(chai_flavor)  # This will display the help information
help(len)


def generate_bill(chai=0, biscuits=0):
    """
    Calculate the total bill for chai and biscuits.

    :param chai: Number of chai cups (10 rupees each)
    :param biscuits: Number of biscuit packets (5 rupees each)
    :return: Total bill amount
    """
    return chai * 10 + biscuits * 5