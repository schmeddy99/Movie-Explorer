import sqlite3

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
