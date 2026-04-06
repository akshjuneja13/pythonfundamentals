# Boolean variable to check if boiling is happening
is_boiling = True

# Integer representing string count
string_count = 5

# Total actions, adding integer and boolean values (True is treated as 1, False as 0)
total_actions = string_count + is_boiling
print(f"Total actions: {total_actions}")

# Variable to check if milk is present
milk_present = 0  # No milk, 0 means False

# Print whether milk is present (False in this case)
print(f"Is milk present: {bool(milk_present)}")

water_hot = True 
tea_added = False  
can_serve_tea = water_hot and tea_added 
print(f"Can serve tea : {can_serve_tea}")