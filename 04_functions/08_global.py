chai_type = "Plain"  # Global variable


def front_desk():
    def kitchen():
        global chai_type  # Refers to global variable
        chai_type = "Masala"

    kitchen()


front_desk()

print(f"Global chai type: {chai_type}")