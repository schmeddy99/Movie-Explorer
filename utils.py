import sqlite3


# Opens a connection to the SQLite database and returns the connection object
def connect_db(path="movie.db"):
    return sqlite3.connect(path)


# Prints query results in a clean format
def print_results(results):
    if not results:
        print("No results found.")
        return

    for row in results:
        print(" | ".join(str(item) for item in row))


def get_or_create_director(conn, name, likes):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM directors WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute(
        "INSERT INTO directors (name, facebook_likes) VALUES (?, ?)", (name, likes)
    )
    return cursor.lastrowid


def get_or_create_actor(conn, name, likes):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM actors WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute(
        "INSERT INTO actors (name, facebook_likes) VALUES (?, ?)", (name, likes)
    )
    return cursor.lastrowid


def get_or_create_genre(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM genres WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    return cursor.lastrowid
