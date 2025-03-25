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
        "SELECT movie_title, director_name FROM MOVIE WHERE LOWER(director_name) LIKE LOWER(?)",
        ("%" + director_name + "%",),
    )
    return cursor.fetchall()


def search_by_genre(conn, genre_substring):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, genres from MOVIE WHERE LOWER(genres) LIKE LOWER(?)",
        ("%" + genre_substring + "%",),
    )
    return cursor.fetchall()


def search_by_year(conn, year):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, title_year from MOVIE WHERE title_year = ?",
        (year,),
    )
    return cursor.fetchall()


def search_by_rating_threshold(conn, min_rating):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, imdb_score from MOVIE WHERE imdb_score > ?",
        (min_rating,),
    )
    return cursor.fetchall()
