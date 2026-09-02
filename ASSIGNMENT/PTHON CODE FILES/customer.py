def add_customer(customers):
    customer_id = input("Enter customer ID: ").strip()

    if customer_id in customers:
        print("Customer already exists.")
        return

    name = input("Enter customer name: ").strip().title()
    location = input("Enter location: ").strip().title()
    city = input("Enter city: ").strip().title()

    # Tuple stores fixed location information
    address = (location, city)

    customers[customer_id] = {
        "name": name,
        "address": address
    }

    print("Customer added successfully.")


def search_customer(customers):
    keyword = input("Enter customer name: ").strip().lower()

    found = False

    for customer_id, details in customers.items():

        if keyword in details["name"].lower():
            print(
                "ID:", customer_id,
                "| Name:", details["name"],
                "| Location:", details["address"]
            )
            found = True

    if not found:
        print("No matching customer found.")