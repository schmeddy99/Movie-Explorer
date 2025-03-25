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
