# Check staff list for adults
# Task: Find the first adult staff member who can manage

staff = [("amit", "16"), ("anu", "17"), ("karan", "18")]

for name, age in staff:
    if int(age) >= 18:
        print(f"{name} is an adult, he/she can manage staff")
        break
else:
    # This else runs only if the loop did not encounter a break
    print("No adults found in the staff list")