import customer
import restaurant
import food
import order
import analysis
import report
import file_handler


# Main data structures

customers = {}

restaurants = {}

food_items = {}

orders = []

cuisines = set()


# Load previously saved data

file_handler.load_data(
    customers,
    restaurants,
    food_items,
    orders,
    cuisines
)


# Main menu

while True:

    print("\n")
    print("========================================")
    print("     ONLINE FOOD ORDER MANAGEMENT")
    print("========================================")

    print("1. Add Customer")
    print("2. Search Customer")

    print("3. Add Restaurant")
    print("4. Search Restaurant")
    print("5. Display Restaurants")

    print("6. Add Food Item")
    print("7. Display Food Menu")

    print("8. Create Order")
    print("9. Change Order Status")
    print("10. Display Orders")

    print("11. Customer Order Value")
    print("12. Compare Orders")

    print("13. Generate Report")

    print("14. Save Data")
    print("15. Exit")

    print("========================================")

    choice = input("Enter your choice: ").strip()

    try:

        if choice == "1":

            customer.add_customer(
                customers
            )


        elif choice == "2":

            customer.search_customer(
                customers
            )


        elif choice == "3":

            restaurant.add_restaurant(
                restaurants
            )


        elif choice == "4":

            restaurant.search_restaurant(
                restaurants
            )


        elif choice == "5":

            restaurant.display_restaurants(
                restaurants
            )


        elif choice == "6":

            food.add_food(
                food_items,
                cuisines,
                restaurants
            )


        elif choice == "7":

            food.display_food(
                food_items,
                restaurants
            )


        elif choice == "8":

            order.create_order(
                customers,
                restaurants,
                food_items,
                orders
            )


        elif choice == "9":

            order.change_status(
                orders
            )


        elif choice == "10":

            order.display_orders(
                customers,
                restaurants,
                food_items,
                orders
            )


        elif choice == "11":

            analysis.show_customer_value(
                customers,
                orders
            )


        elif choice == "12":

            analysis.compare_orders(
                orders
            )


        elif choice == "13":

            report.generate_report(
                customers,
                restaurants,
                food_items,
                orders,
                cuisines
            )


        elif choice == "14":

            file_handler.save_data(
                customers,
                restaurants,
                food_items,
                orders
            )


        elif choice == "15":

            file_handler.save_data(
                customers,
                restaurants,
                food_items,
                orders
            )

            print("Program closed.")

            break


        else:

            print("Please select a valid option.")


    except order.OrderError as error:

        print(
            "Order Error:",
            error
        )


    except Exception as error:

        print(
            "Unexpected error:",
            error
        )