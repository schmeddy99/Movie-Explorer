import sqlite3

import queries.queries as queries
import queries.fun_queries as discover
import import_data
import schema
import utils
import menus

"""
main.py

Entry point for the CLI movie tool.
Handles DB setup and displays the main menu loop.
"""


def main_menu(conn):
    """
    Displays the main menu and routes user input to submenus.
    """
    while True:
        menu_choice = input(
            "\nChoose an option:\n"
            "1. Search (by title, director, etc)\n"
            "2. Insights (top-rated, averages, trends)\n"
            "3. Discovery (random, stats, surprises)\n"
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
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")


# ------------------------------
# 1. Connect to the database
# ------------------------------
try:
    conn = utils.connect_db()

    schema.create_all_tables(conn)
    import_data.populate_normalized_db(conn)

    # ------------------------------
    # 2. Run the interactive menu
    # ------------------------------
    main_menu(conn)

# ------------------------------
# 3. Handle errors
# ------------------------------
except sqlite3.Error as error:
    print("Error occurred -", error)

# ------------------------------
# 4. Close the connection
# ------------------------------
finally:
    if conn:
        conn.close()
        print("SQLite Connection closed")
