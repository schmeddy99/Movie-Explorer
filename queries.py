import sqlite3
import main

# Contains SQL query functions for searching and filtering movie data.


def search_by_title(conn, title_substring):
    # Write a query and execute it with cursor
    query = "SELECT movie_title FROM MOVIE"
    main.cursor.execute(query)
