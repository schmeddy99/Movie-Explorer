import sqlite3


try:
    # Connect to DB and create a cursor
    conn = sqlite3.connect("movie.db")
    cursor = conn.cursor()
    print("DB INIT")

    # Fetch and output result
    results = cursor.fetchall()
    print(results)

    # Close the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print("Error occured -", error)

# Close DB Connection irrespective of success
# or failure
finally:
    if conn:
        conn.close()
        print("SQLite Connection closed")
