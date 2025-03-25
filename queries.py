import sqlite3

# Contains SQL query functions for searching and filtering movie data.


# Uses LIKE for partial match
def search_by_title(conn, title_substring):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title FROM MOVIE WHERE movie_title LIKE ?",
        ("%" + title_substring + "%",),
    )
    return cursor.fetchall()


# Case-insensitive search with LOWER()
def search_by_director(conn, director_name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT DISTINCT director_name FROM MOVIE WHERE LOWER(director_name) LIKE LOWER(?)",
        ("%" + director_name + "%",),
    )
    return cursor.fetchall()
