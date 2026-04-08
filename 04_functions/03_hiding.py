# Task:
# Separate concerns:
# 1. get_input() - gets user input
# 2. validate_input() - checks if the input is valid
# 3. save_to_db() - saves the user data


def get_input():
    print("Getting user input...")
    return input("Enter your name: ")


def validate_input(user_input):
    print("Validating user input...")

    if not user_input.strip():
        print("Invalid input: cannot be empty.")
        return False

    return True


def save_to_db(user_input):
    print("Saving user data to database...")
    # Simulated save
    print(f"User '{user_input}' saved successfully!")