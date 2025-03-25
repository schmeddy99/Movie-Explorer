import sqlite3


import queries
import import_data
import schema

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
            print(results)
        elif option == "2":
            director = input("Enter a director to search: ")
            results = queries.search_by_director(conn, director)
            print(results)
        elif option == "6":
            print("Goodbye")
            break


# ------------------------------
# 1. Connect to the database
# ------------------------------
try:
    # Connect to DB and create a cursor
    conn = sqlite3.connect("movie.db")

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
