def add_food(food_items, cuisines, restaurants):

    code = input("Enter food code: ").strip().upper()

    if code in food_items:
        print("Food item already exists.")
        return

    restaurant_id = input("Enter restaurant ID: ").strip().upper()

    if restaurant_id not in restaurants:
        print("Restaurant does not exist.")
        return

    name = input("Enter food name: ").strip().title()

    if not name:
        print("Food name cannot be empty.")
        return

    category = input("Enter cuisine category: ").strip().title()

    if not category:
        print("Cuisine category cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))

        if price <= 0:
            print("Price must be positive.")
            return

    except ValueError:
        print("Please enter a valid price.")
        return

    food_items[code] = {
        "name": name,
        "category": category,
        "price": price,
        "restaurant": restaurant_id
    }

    cuisines.add(category)

    print("Food item added successfully.")


def display_food(food_items, restaurants):

    if not food_items:
        print("No food items available.")
        return

    print("\n---------- FOOD MENU ----------")

    for code, item in food_items.items():

        restaurant_id = item["restaurant"]

        if restaurant_id in restaurants:
            restaurant_name = restaurants[restaurant_id]["name"]
        else:
            restaurant_name = "Unknown"

        print(
            code,
            "|",
            item["name"],
            "|",
            item["category"],
            "| Restaurant:",
            restaurant_name,
            "| Rs.",
            item["price"]
        )