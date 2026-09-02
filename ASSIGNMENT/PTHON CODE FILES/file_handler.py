import csv


def save_data(customers, restaurants, food_items, orders):

    with open(
        "customers.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Location",
            "City"
        ])

        for customer_id, details in customers.items():

            writer.writerow([
                customer_id,
                details["name"],
                details["address"][0],
                details["address"][1]
            ])


    with open(
        "restaurants.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Location"
        ])

        for restaurant_id, details in restaurants.items():

            writer.writerow([
                restaurant_id,
                details["name"],
                details["location"]
            ])


    with open(
        "food_items.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Code",
            "Name",
            "Category",
            "Price",
            "Restaurant"
        ])

        for code, item in food_items.items():

            writer.writerow([
                code,
                item["name"],
                item["category"],
                item["price"],
                item["restaurant"]
            ])


    with open(
        "orders.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Customer",
            "Restaurant",
            "Food",
            "Quantity",
            "Status",
            "Subtotal",
            "Discount",
            "Delivery",
            "Total"
        ])

        for order in orders:

            writer.writerow([
                order["customer"],
                order["restaurant"],
                order["food"],
                order["quantity"],
                order["status"],
                order["subtotal"],
                order["discount"],
                order["delivery"],
                order["total"]
            ])

    print("All data saved successfully.")


def load_data(
    customers,
    restaurants,
    food_items,
    orders,
    cuisines
):

    try:

        with open(
            "customers.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                customers[row["ID"]] = {
                    "name": row["Name"],
                    "address": (
                        row["Location"],
                        row["City"]
                    )
                }


        try:

            with open(
                "restaurants.csv",
                "r"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    restaurants[row["ID"]] = {
                        "name": row["Name"],
                        "location": row["Location"]
                    }

        except FileNotFoundError:
            print("No previous restaurant data found.")


        with open(
            "food_items.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                food_items[row["Code"]] = {
                    "name": row["Name"],
                    "category": row["Category"],
                    "price": float(row["Price"]),
                    "restaurant": row["Restaurant"]
                }

                cuisines.add(row["Category"])


        with open(
            "orders.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                orders.append({
                    "customer": row["Customer"],
                    "restaurant": row["Restaurant"],
                    "food": row["Food"],
                    "quantity": int(row["Quantity"]),
                    "status": row["Status"],
                    "subtotal": float(row["Subtotal"]),
                    "discount": float(row["Discount"]),
                    "delivery": float(row["Delivery"]),
                    "total": float(row["Total"])
                })

        print("Previous data loaded.")

    except FileNotFoundError:
        print("No previous data found.")

    except Exception as error:
        print("Error while loading:", error)