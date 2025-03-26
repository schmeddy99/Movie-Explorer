import sqlite3

# Contains SQL query functions for searching and filtering movie data.


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
    Searches for movies directed by names matching the given input.
    Case-insensitive. Results include director name and movie title.
    """

    cursor = conn.cursor()
    cursor.execute(
        "SELECT director_name, movie_title FROM MOVIE WHERE LOWER(director_name) LIKE LOWER(?) ORDER BY director_name ASC",
        ("%" + director_name + "%",),
    )
    return cursor.fetchall()


def search_by_genre(conn, genre_substring):
    """
    Searches for movies that contain the given genre substring.
    Case-insensitive. Returns movie title and full genre string.
    """

    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, genres from MOVIE WHERE LOWER(genres) LIKE LOWER(?) ORDER BY movie_title ASC",
        ("%" + genre_substring + "%",),
    )
    return cursor.fetchall()


def search_by_year(conn, year):
    """
    Retrieves movies released in the given year.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, title_year from MOVIE WHERE title_year = ?",
        (year,),
    )
    return cursor.fetchall()


def search_by_rating_threshold(conn, min_rating):
    """
    Retrieves movies with an IMDb score above the given threshold.
    Results are sorted alphabetically by title.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT movie_title, imdb_score from MOVIE WHERE imdb_score > ? ORDER BY movie_title ASC",
        (min_rating,),
    )
    return cursor.fetchall()


def get_top_rated_movies(conn, limit):
    """
    Returns the top N highest-rated movies by IMDb score.
    Results include movie title, genres, and score.
    """
    cursor = conn.cursor()
    cursor.execute(
        ""
        "SELECT movie_title, genres, imdb_score from MOVIE ORDER BY imdb_score DESC LIMIT ?",
        (limit,),
    )
    return cursor.fetchall()


def get_average_rating_by_genre(conn):
    """
    Calculates the average IMDb rating for each genre.
    Results are sorted by average score in descending order.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT genres, AVG(imdb_score) from MOVIE GROUP BY genres ORDER BY AVG(imdb_score) DESC"
    )
    return cursor.fetchall()


def get_movies_per_decade(conn):
    """
    Counts the number of movies released in each decade.
    Returns decade and total count, sorted by decade ascending.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT (title_year / 10) * 10 AS decade,COUNT(*) FROM MOVIE WHERE title_year IS NOT NULL GROUP BY decade ORDER BY decade ASC"
    )
    return cursor.fetchall()


def most_frequent_director(conn):
    """
    Returns the director with the highest number of movies in the dataset.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT director_name, COUNT(*) AS movie_count from MOVIE WHERE director_name IS NOT NULL GROUP BY director_name ORDER BY movie_count DESC LIMIT 1"
    )
    return cursor.fetchall()


def get_avg_gross_by_country(conn):
    """
    Calculates the average gross earnings per country (where gross is available).
    Results are sorted by average gross descending.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT country, AVG(gross) from MOVIE WHERE gross IS NOT NULL GROUP BY country ORDER BY AVG(gross) DESC"
    )
    return cursor.fetchall()
