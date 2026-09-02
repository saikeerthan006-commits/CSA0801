def add_restaurant(restaurants):
    restaurant_id = input("Enter restaurant ID: ").strip().upper()

    if restaurant_id in restaurants:
        print("Restaurant already exists.")
        return

    name = input("Enter restaurant name: ").strip().title()

    if not name:
        print("Restaurant name cannot be empty.")
        return

    location = input("Enter restaurant location: ").strip().title()

    if not location:
        print("Restaurant location cannot be empty.")
        return

    restaurants[restaurant_id] = {
        "name": name,
        "location": location
    }

    print("Restaurant added successfully.")


def search_restaurant(restaurants):
    keyword = input("Enter restaurant name: ").strip().lower()

    found = False

    for restaurant_id, details in restaurants.items():

        if keyword in details["name"].lower():
            print(
                "ID:", restaurant_id,
                "| Name:", details["name"],
                "| Location:", details["location"]
            )

            found = True

    if not found:
        print("No matching restaurant found.")


def display_restaurants(restaurants):

    if not restaurants:
        print("No restaurants available.")
        return

    print("\n---------- RESTAURANT LIST ----------")

    for restaurant_id, details in restaurants.items():

        print(
            restaurant_id,
            "|",
            details["name"],
            "|",
            details["location"]
        )