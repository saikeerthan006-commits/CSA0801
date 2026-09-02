class OrderError(Exception):
    pass


def create_order(customers, restaurants, food_items, orders):

    customer_id = input("Enter customer ID: ").strip()

    if customer_id not in customers:
        raise OrderError("Customer ID does not exist.")

    food_code = input("Enter food code: ").strip().upper()

    if food_code not in food_items:
        raise OrderError("Food code does not exist.")

    restaurant_id = food_items[food_code]["restaurant"]

    if restaurant_id not in restaurants:
        raise OrderError("Restaurant does not exist.")

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

    except ValueError:
        raise OrderError("Quantity must be a positive integer.")

    price = food_items[food_code]["price"]

    subtotal = price * quantity

    if subtotal >= 1000:
        discount = subtotal * 0.10

    elif subtotal >= 500:
        discount = subtotal * 0.05

    else:
        discount = 0

    delivery_charge = 40

    total = subtotal - discount + delivery_charge

    new_order = {
        "customer": customer_id,
        "restaurant": restaurant_id,
        "food": food_code,
        "quantity": quantity,
        "status": "Pending",
        "subtotal": subtotal,
        "discount": discount,
        "delivery": delivery_charge,
        "total": total
    }

    orders.append(new_order)

    print("\nOrder created successfully.")
    print("Restaurant:", restaurants[restaurant_id]["name"])
    print("Food:", food_items[food_code]["name"])
    print("Final amount: Rs.", round(total, 2))


def display_orders(customers, restaurants, food_items, orders):

    if not orders:
        print("No orders available.")
        return

    print("\n---------- ORDER LIST ----------")

    for number, order in enumerate(orders, start=1):

        customer_name = customers[
            order["customer"]
        ]["name"]

        food_name = food_items[
            order["food"]
        ]["name"]

        restaurant_name = restaurants[
            order["restaurant"]
        ]["name"]

        print(
            number,
            "| Customer:", customer_name,
            "| Restaurant:", restaurant_name,
            "| Food:", food_name,
            "| Qty:", order["quantity"],
            "| Status:", order["status"],
            "| Rs.", round(order["total"], 2)
        )


def change_status(orders):

    if not orders:
        print("There are no orders.")
        return

    for number, order in enumerate(orders, start=1):

        print(
            number,
            order["food"],
            order["status"]
        )

    try:
        number = int(input("Enter order number: "))

        if number < 1 or number > len(orders):
            raise ValueError

    except ValueError:
        print("Invalid order number.")
        return

    status = input(
        "Enter new status: "
    ).strip().title()

    valid_status = (
        "Pending",
        "Confirmed",
        "Preparing",
        "Delivered",
        "Cancelled"
    )

    if status not in valid_status:
        print("Invalid status.")
        return

    orders[number - 1]["status"] = status

    print("Order status updated.")