import sqlite3
import json
import os


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


def export_to_json(results, filename="export.json"):
    """
    Exports results (list of tuples) to a JSON file.
    """
    try:
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)
        print(f"✅ Results exported to {filename}")
    except Exception as e:
        print(f"❌ Failed to export JSON: {e}")


def export_to_html(results, filename="export.html"):
    """
    Exports results to a simple HTML table.
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
