chai_type = "ginger"  # Global


def update_order():
    chai_type = "lemon"  # Enclosing

    def kitchen():
        nonlocal chai_type
        chai_type = "masala"

    kitchen()
    print(f"Updated order in update_order: {chai_type}")


update_order()