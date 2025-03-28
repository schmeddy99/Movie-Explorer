import sqlite3
import json
import os

# --------------------------------------------
# Utility functions for DB connection, printing,
# reusable lookups, and exporting results
# --------------------------------------------


def connect_db(path="movie.db"):
    """
    Opens a connection to the SQLite database.
    Returns a connection object.
    """
    return sqlite3.connect(path)


def print_results(results):
    """
    Prints query results (list of tuples) in a clean, readable format.
    """
    if not results:
        print("No results found.")
        return

    for row in results:
        print(" | ".join(str(item) for item in row))


def get_or_create_director(conn, name, likes):
    """
    Returns the director ID if they exist, otherwise inserts and returns new ID.
    """
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
    """
    Returns the actor ID if they exist, otherwise inserts and returns new ID.
    """
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
    """
    Returns the genre ID if it exists, otherwise inserts and returns new ID.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM genres WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    return cursor.lastrowid


def export_to_json(results, filename="export.json"):
    """
    Exports a list of tuples (results) to a .json file.
    """
    try:
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)
        print(f"✅ Results exported to {filename}")
    except Exception as e:
        print(f"❌ Failed to export JSON: {e}")


def export_to_html(results, filename="export.html"):
    """
    Exports a list of tuples (results) to a .html table.
    """
    try:
        with open(filename, "w") as f:
            f.write("<html><body><table border='1'>\n")
            for row in results:
                f.write("<tr>" + "".join(f"<td>{col}</td>" for col in row) + "</tr>\n")
            f.write("</table></body></html>")
        print(f"✅ Results exported to {filename}")
    except Exception as e:
        print(f"❌ Failed to export HTML: {e}")
