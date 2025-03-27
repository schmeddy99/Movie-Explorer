import sqlite3


import queries.queries as queries
import queries.fun_queries as discover
import import_data
import schema
import utils
import menus


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
            "3. Discovery ()"
            "4. Exit\n"
            "Command: "
        )
        if menu_choice == "1":
            menus.search_menu(conn)
        elif menu_choice == "2":
            menus.insights_menu(conn)
        elif menu_choice == "3":
            menus.discovery_menu(conn)
        elif menu_choice == "4":
            break
        else:
            print("Invalid selection. Please try again. ")


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
