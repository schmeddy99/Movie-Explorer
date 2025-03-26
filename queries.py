import sqlite3

# Contains SQL query functions for searching and filtering movie data.


# Uses LIKE for partial match
def search_by_title(conn, title_substring):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title FROM MOVIE WHERE movie_title LIKE ? ORDER BY movie_title ASC",
        ("%" + title_substring + "%",),
    )
    return cursor.fetchall()


# Case-insensitive search with LOWER()
def search_by_director(conn, director_name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT director_name, movie_title FROM MOVIE WHERE LOWER(director_name) LIKE LOWER(?) ORDER BY director_name ASC",
        ("%" + director_name + "%",),
    )
    return cursor.fetchall()


def search_by_genre(conn, genre_substring):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, genres from MOVIE WHERE LOWER(genres) LIKE LOWER(?) ORDER BY movie_title ASC",
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
        "SELECT movie_title, imdb_score from MOVIE WHERE imdb_score > ? ORDER BY movie_title ASC",
        (min_rating,),
    )
    return cursor.fetchall()


def get_top_rated_movies(conn, limit):
    cursor = conn.cursor()
    cursor.execute(
        ""
        "SELECT movie_title, genres, imdb_score from MOVIE ORDER BY imdb_score DESC LIMIT ?",
        (limit,),
    )
    return cursor.fetchall()


def get_average_rating_by_genre(conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT genres, AVG(imdb_score) from MOVIE GROUP BY genres ORDER BY AVG(imdb_score) DESC"
    )
    return cursor.fetchall()
