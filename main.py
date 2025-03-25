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
        option = input(
            "Choose an option:\n "
            "1. Search by title\n "
            "2. Search by director\n "
            "3. Filter by genre\n "
            "4. Filter by year\n "
            "5. Filter by rating\n "
            "6. Exit\n"
            "Command: "
        )
        if option == "1":
            title = input("Enter a movie title to search: ")
            results = queries.search_by_title(conn, title)
            utils.print_results(results)
        elif option == "2":
            director = input("Enter a director to search: ")
            results = queries.search_by_director(conn, director)
            utils.print_results(results)
        elif option == "3":
            genre = input("Enter a genre: ")
            results = queries.search_by_genre(conn, genre)
            utils.print_results(results)
        elif option == "4":
            year = input("Enter a year: ")
            if not year.isdigit():
                print("Please enter a valid year.")
                continue
            results = queries.search_by_year(conn, int(year))
            utils.print_results(results)
        elif option == "5":
            rating = int(input("Enter a minimum rating: "))
            results = queries.search_by_rating_threshold(conn, rating)
            utils.print_results(results)
        elif option == "6":
            print("Goodbye")
            break
        else:
            print("Invalid selection. Please try again. ")


# ------------------------------
# 1. Connect to the database
# ------------------------------
try:
    # Connect to DB and create a cursor
    conn = utils.connect_db()

    schema.create_movie_table(conn)
    import_data.populate_db(conn)

    main_menu(conn)
    # ------------------------------
    # 3. Handle user input
    #    - Call appropriate function from queries.py
    #    - Ask for any needed input (e.g., title, director, genre)
    # ------------------------------


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
