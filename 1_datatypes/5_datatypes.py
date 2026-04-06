import sys
from fractions import Fraction
from decimal import Decimal

# Float values for temperatures
ideal_temp = 95.5
current_temp = 95.490090909090

# Display current temperature and difference from ideal temperature
print(f"Current temperature: {current_temp}, ideal temperature: {ideal_temp}")
print(f"Difference: {ideal_temp - current_temp}")

# Display system float information (precision, etc.)
print(sys.float_info)

# Skipping complex numbers section for now