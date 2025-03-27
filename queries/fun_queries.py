import sqlite3
from collections import Counter


# Fun queries for random movie discovery


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
    Returns a random movie where the genre matches the input.
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
    Returns a random movie from the specified decade start year (e.g. 1990).
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
    Returns the movie with the longest title (by character length).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, LENGTH(title) as title_length
        FROM movies
        ORDER BY title_length DESC
        LIMIT 1
        """
    )
    return cursor.fetchall()


def get_most_common_genre_word(conn):
    """
    Splits genre names and returns the most common word used across all genres.
    Useful for seeing popular themes (e.g., 'Drama', 'Action').
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

    most_common = Counter(words).most_common(1)
    return most_common  # Returns list of (word, count)


def count_words_in_titles(conn):
    """
    Counts the total number of words across all movie titles in the database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies")
    titles = cursor.fetchall()

    word_count = 0
    for (title,) in titles:
        if title:
            word_count += len(title.split())

    return word_count
