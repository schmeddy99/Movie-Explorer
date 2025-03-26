import sqlite3


import queries
import import_data
import schema
import utils


# Main entry point for running the CLI movie search tool.
def main_menu(conn):
    while True:

        # ------------------------------
        # 2. Display the main menu
        #    - Show user options
        #    - Use input() to get choice
        # ------------------------------
        menu_choice = input(
            "Choose an option:\n"
            "1. Search (by title, director, etc)\n"
            "2. Insights (top-rated, averages, trends)\n"
            "3. Exit\n"
            "Command: "
        )
        if menu_choice == "1":
            search_menu(conn)
        elif menu_choice == "2":
            insights_menu(conn)
        elif menu_choice == "3":
            break
        else:
            print("Invalid selection. Please try again. ")


def search_menu(conn):
    while True:
        search_choice = input(
            "Choose an option:\n "
            "1. Search by title\n "
            "2. Search by director\n "
            "3. Filter by genre\n "
            "4. Filter by year\n "
            "5. Filter by rating\n "
            "6. Exit\n"
            "Command: "
        )
        if search_choice == "1":
            title = input("Enter a movie title to search: ")
            results = queries.search_by_title(conn, title)
            utils.print_results(results)
        elif search_choice == "2":
            director = input("Enter a director to search: ")
            results = queries.search_by_director(conn, director)
            utils.print_results(results)
        elif search_choice == "3":
            genre = input("Enter a genre: ")
            results = queries.search_by_genre(conn, genre)
            utils.print_results(results)
        elif search_choice == "4":
            year = input("Enter a year: ")
            if not year.isdigit():
                print("Please enter a valid year.")
                continue
            results = queries.search_by_year(conn, int(year))
            utils.print_results(results)
        elif search_choice == "5":
            rating = int(input("Enter a minimum rating: "))
            results = queries.search_by_rating_threshold(conn, rating)
            utils.print_results(results)
        elif search_choice == "6":
            break
        else:
            print("Invalid selection. Please try again. ")


def insights_menu(conn):
    while True:
        insights_choice = input(
            "\n--- Movie Insights ---\n"
            "a. Top rated movies\n"
            "b. Average rating by genre\n"
            "c. Movies per decade\n"
            "d. Most frequent director\n"
            "e. Average gross by country\n"
            "f. Back to main menu\n"
            "Command: "
        )

        if insights_choice == "a":
            limit = input("How many top-rated movies do you want to see? ")
            if not limit.isdigit():
                print("Please enter a valid number.")
                continue
            results = queries.get_top_rated_movies(conn, int(limit))
            utils.print_results(results)

        elif insights_choice == "b":
            results = queries.get_average_rating_by_genre(conn)
            utils.print_results(results)

        elif insights_choice == "c":
            results = queries.get_movies_per_decade(conn)
            utils.print_results(results)

        elif insights_choice == "d":
            results = queries.most_frequent_director(conn)
            utils.print_results(results)

        elif insights_choice == "e":
            results = queries.get_avg_gross_by_country(conn)
            utils.print_results(results)

        elif insights_choice == "f":
            break

        else:
            print("Invalid selection. Please try again.")


# ------------------------------
# 1. Connect to the database
# ------------------------------
try:
    # Connect to DB and create a cursor
    conn = utils.connect_db()

    schema.create_all_tables(conn)
    import_data.populate_normalized_db(conn)

    # ------------------------------
    # 3. Handle user input
    #    - Call appropriate function from queries.py
    #    - Ask for any needed input (e.g., title, director, genre)
    # ------------------------------
    main_menu(conn)

# ------------------------------
# 4. Print results
#    - Format and display output cleanly
# ------------------------------

# ------------------------------
# 5. Loop until user exits
# ------------------------------


# Handle errors
except sqlite3.Error as error:
    print("Error occured -", error)


# ------------------------------
# 6. Close the connection
# ------------------------------

# Close DB Connection irrespective of success
# or failure
finally:
    if conn:
        conn.close()
        print("SQLite Connection closed")
