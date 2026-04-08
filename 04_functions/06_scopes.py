# Global scope (G)
chai_type = "Ginger Chai"


def serve_chai():
    # Local scope (L)
    chai_type = "Masala Chai"
    print(f"Serving {chai_type}")


serve_chai()  # Uses local variable
print(f"Global chai type: {chai_type}")  # Uses global variable


def chai_encounter():
    # Enclosing scope (E)
    chai_order = "Lemon Chai"

    def prepare_chai():
        # Local scope (L inside nested function)
        print(f"Preparing {chai_order}")  # Uses enclosing variable

    prepare_chai()


chai_encounter()