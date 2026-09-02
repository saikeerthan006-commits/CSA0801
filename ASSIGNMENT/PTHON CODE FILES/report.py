def generate_report(
    customers,
    restaurants,
    food_items,
    orders,
    cuisines
):

    print("\n================================")
    print("       FOOD ORDER REPORT")
    print("================================")

    print("Total customers  :", len(customers))
    print("Total restaurants:", len(restaurants))
    print("Total food items :", len(food_items))
    print("Total orders     :", len(orders))

    sales = 0

    status_count = {}

    restaurant_sales = {}

    for order in orders:

        sales += order["total"]

        status = order["status"]

        if status not in status_count:
            status_count[status] = 0

        status_count[status] += 1

        restaurant_id = order["restaurant"]

        if restaurant_id not in restaurant_sales:
            restaurant_sales[restaurant_id] = 0

        restaurant_sales[restaurant_id] += order["total"]


    print(
        "Total sales      : Rs.",
        round(sales, 2)
    )


    print("\nOrder Status:")

    for status, count in status_count.items():

        print(
            status,
            ":",
            count
        )


    print("\nRestaurant Performance:")

    for restaurant_id, amount in restaurant_sales.items():

        if restaurant_id in restaurants:

            print(
                restaurants[restaurant_id]["name"],
                ": Rs.",
                round(amount, 2)
            )


    print("\nCuisine Categories:")

    for category in sorted(cuisines):

        print("-", category)


    print("================================")