import sqlite3


# Opens a connection to the SQLite database and returns the connection object
def connect_db(path="movie.db"):
    return sqlite3.connect(path)
