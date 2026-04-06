# String is immutable

chai_type = "Ginger"
customer_name = "John Doe"

# Print order details
print(f"Order from {customer_name} for {chai_type}")

# Chai description
chai_description = "Aromatic and Bold"

# String slicing
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[9:13]}")
print(f"Chai description: {chai_description[0:17]}")

# Reverse the string
print(f"Chai description (reversed): {chai_description[::-1]}")

# Special characters and encoding
# Mandarin and Chinese characters may look fine in terminal,
# but proper encoding (UTF-8) is recommended

greetings = 'label text "Chai Special"'
encoded_label = greetings.encode("utf-8")
print(f"Encoded label : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")