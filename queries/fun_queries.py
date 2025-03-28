import sqlite3
from collections import Counter

# -------------------------------------------------------------
# fun_queries.py
# -------------------------------------------------------------
# Contains playful and exploratory SQL queries for discovering
# random movies, long titles, genre word trends, and fun stats.
# -------------------------------------------------------------


def get_random_movie(conn):
    """
    Returns one random movie from the database.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT title, year, imdb_score FROM movies ORDER BY RANDOM() LIMIT 1"
    )
    return cursor.fetchall()


def get_random_movie_by_genre(conn, genre):
    """
    Returns a random movie from a given genre.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT m.title, m.year, m.imdb_score
        FROM movies m
        JOIN movie_genres mg ON m.id = mg.movie_id
        JOIN genres g ON g.id = mg.genre_id
        WHERE LOWER(g.name) LIKE LOWER(?)
        ORDER BY RANDOM() LIMIT 1
        """,
        ("%" + genre + "%",),
    )
    return cursor.fetchall()


def get_random_movie_by_decade(conn, decade_start):
    """
    Returns a random movie from a specific decade (e.g., 1990s).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, year, imdb_score
        FROM movies
        WHERE year BETWEEN ? AND ?
        ORDER BY RANDOM() LIMIT 1
        """,
        (decade_start, decade_start + 9),
    )
    return cursor.fetchall()


def get_longest_movie_title(conn):
    """
    Returns the movie with the longest title by character count.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, LENGTH(title) AS title_length
        FROM movies
        ORDER BY title_length DESC
        LIMIT 1
        """
    )
    return cursor.fetchall()


def get_most_common_genre_word(conn):
    """
    Returns the most frequent word found across all genre names.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM genres")
    genres = cursor.fetchall()

    words = []
    for (genre,) in genres:
        if genre:
            words.extend(genre.lower().split())

    if not words:
        return []

    return Counter(words).most_common(1)  # [(word, count)]


def count_words_in_titles(conn):
    """
    Counts the total number of words across all movie titles.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies")
    titles = cursor.fetchall()

    word_count = sum(len(title.split()) for (title,) in titles if title)
    return word_count
