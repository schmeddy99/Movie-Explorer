import sqlite3

# -------------------------------------------------------------
# queries.py
# -------------------------------------------------------------
# Contains SQL query functions for filtering and analyzing movie data.
# Covers basic search, filters, and grouped statistical queries.
# -------------------------------------------------------------


def search_by_title(conn, title_substring):
    """
    Searches for movies with titles containing the given substring.
    Results are sorted alphabetically by movie title.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title FROM MOVIE WHERE movie_title LIKE ? ORDER BY movie_title ASC",
        ("%" + title_substring + "%",),
    )
    return cursor.fetchall()


def search_by_director(conn, director_name):
    """
    Searches for movies by directors matching the input (case-insensitive).
    Returns pairs of (director_name, movie_title), sorted by director.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT director_name, movie_title FROM MOVIE WHERE LOWER(director_name) LIKE LOWER(?) ORDER BY director_name ASC",
        ("%" + director_name + "%",),
    )
    return cursor.fetchall()


def search_by_genre(conn, genre_substring):
    """
    Searches for movies whose genres contain the given substring (case-insensitive).
    Returns movie title and the full genre string.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, genres FROM MOVIE WHERE LOWER(genres) LIKE LOWER(?) ORDER BY movie_title ASC",
        ("%" + genre_substring + "%",),
    )
    return cursor.fetchall()


def search_by_year(conn, year):
    """
    Returns all movies released in the given year.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, title_year FROM MOVIE WHERE title_year = ?",
        (year,),
    )
    return cursor.fetchall()


def search_by_rating_threshold(conn, min_rating):
    """
    Returns movies with an IMDb score greater than the given minimum.
    Results are sorted alphabetically by movie title.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, imdb_score FROM MOVIE WHERE imdb_score > ? ORDER BY movie_title ASC",
        (min_rating,),
    )
    return cursor.fetchall()


def get_top_rated_movies(conn, limit):
    """
    Returns the top N movies by IMDb score, highest first.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, genres, imdb_score FROM MOVIE ORDER BY imdb_score DESC LIMIT ?",
        (limit,),
    )
    return cursor.fetchall()


def get_average_rating_by_genre(conn):
    """
    Calculates the average IMDb score for each genre group.
    Results are ordered by average score descending.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT genres, AVG(imdb_score) FROM MOVIE GROUP BY genres ORDER BY AVG(imdb_score) DESC"
    )
    return cursor.fetchall()


def get_movies_per_decade(conn):
    """
    Groups movies by decade and counts the number in each.
    Example: 1990s → 1990–1999
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT (title_year / 10) * 10 AS decade, COUNT(*) FROM MOVIE WHERE title_year IS NOT NULL GROUP BY decade ORDER BY decade ASC"
    )
    return cursor.fetchall()


def most_frequent_director(conn):
    """
    Returns the director with the most movies in the dataset.
    Includes the count of their movies.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT director_name, COUNT(*) AS movie_count FROM MOVIE WHERE director_name IS NOT NULL GROUP BY director_name ORDER BY movie_count DESC LIMIT 1"
    )
    return cursor.fetchall()


def get_avg_gross_by_country(conn):
    """
    Calculates average gross earnings by country (excluding nulls).
    Sorted by average gross descending.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT country, AVG(gross) FROM MOVIE WHERE gross IS NOT NULL GROUP BY country ORDER BY AVG(gross) DESC"
    )
    return cursor.fetchall()
