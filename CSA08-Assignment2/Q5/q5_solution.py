"""
Q5 - Functions, Parameters and Scope
College Canteen Order System
"""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    # TODO 1: Create a new empty list when order is None, append the item and return
    # the list
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(prices: list[float], gst_rate: float = 0.05, discount: float = 0.0) -> tuple[float, float, float]:
    """Demonstrates positional, default, keyword args and multiple return values (tuple)."""
    subtotal = sum(prices) - discount
    gst = round(subtotal * gst_rate, 2)
    grand_total = round(subtotal + gst, 2)
    return subtotal, gst, grand_total

# Scope Demonstration (LEGB: Local, Enclosing/nonlocal, Global, Built-in)
canteen_name = "Campus Central Canteen"  # Global variable
total_orders_served = 0

def demonstrate_scope():
    global total_orders_served
    total_orders_served += 1  # Requires 'global' to rebind module-level variable
    counter_label = "Order Counter"  # Enclosing (nonlocal) variable

    def inner_logger():
        nonlocal counter_label
        local_msg = f"[{canteen_name}] {counter_label} #{total_orders_served}"  # Local variable
        counter_label = "Updated Counter"
        return local_msg

    return inner_logger(), counter_label

def make_order_closure():
    """Alternative Concept: Managing order state inside a closure."""
    items = []
    def add(item: str) -> list[str]:
        items.append(item)
        return list(items)
    return add

if __name__ == "__main__":
    print("--- Complete the Code Output ---")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print(add_item("Tea"), add_item("Vada"))
    print("add_item_buggy.__defaults__ after calls:", add_item_buggy.__defaults__)

    print("\n--- Testing 3 Independent Customers ---")
    cust1 = add_item("Masala Dosa")
    add_item("Filter Coffee", cust1)

    cust2 = add_item("Idli Sambar")

    cust3 = add_item("Veg Biryani")
    add_item("Lemon Soda", cust3)

    print("Customer 1 Order:", cust1)
    print("Customer 2 Order:", cust2)
    print("Customer 3 Order:", cust3)

    sub, gst, total = calculate_bill([60.0, 25.0], gst_rate=0.05, discount=5.0)
    print(f"Bill Summary -> Subtotal: Rs.{sub}, GST: Rs.{gst}, Total: Rs.{total}")

    msg, updated_label = demonstrate_scope()
    print("Scope Demo:", msg, "| Enclosing variable after nonlocal:", updated_label)
