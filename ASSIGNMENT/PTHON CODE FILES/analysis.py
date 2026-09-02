def customer_order_value(customer_id, orders):

    total = 0

    for order in orders:

        if order["customer"] == customer_id:
            total += order["total"]

    return total


def show_customer_value(customers, orders):

    customer_id = input("Enter customer ID: ").strip()

    if customer_id not in customers:
        print("Customer not found.")
        return

    amount = customer_order_value(
        customer_id,
        orders
    )

    print(
        customers[customer_id]["name"],
        "has ordered goods worth Rs.",
        round(amount, 2)
    )


def compare_orders(orders):

    if len(orders) < 2:
        print("At least two orders are required.")
        return

    try:
        first = int(input("Enter first order number: "))
        second = int(input("Enter second order number: "))

        if (
            first < 1
            or first > len(orders)
            or second < 1
            or second > len(orders)
        ):
            raise ValueError

    except ValueError:
        print("Invalid order number.")
        return

    amount_one = orders[first - 1]["total"]
    amount_two = orders[second - 1]["total"]

    if amount_one > amount_two:
        print("First order has the higher value.")

    elif amount_two > amount_one:
        print("Second order has the higher value.")

    else:
        print("Both orders have equal value.")