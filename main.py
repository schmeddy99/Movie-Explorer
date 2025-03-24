import sqlite3
import csv


try:
    # Connect to DB and create a cursor
    conn = sqlite3.connect("movie.db")
    cursor = conn.cursor()
    print("DB INIT")

    # Drop table if it exists
    cursor.execute("DROP TABLE IF EXISTS MOVIE")

    # Create the table if it doesn't exist (optional)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS MOVIE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color TEXT,
            director_name TEXT,
            num_critic_for_reviews INTEGER,
            duration INTEGER,
            director_facebook_likes INTEGER,
            actor_3_facebook_likes INTEGER,
            actor_2_name TEXT,
            actor_1_facebook_likes INTEGER,
            gross INTEGER,
            genres TEXT,
            actor_1_name TEXT,
            movie_title TEXT,
            num_voted_users INTEGER,
            cast_total_facebook_likes INTEGER,
            actor_3_name TEXT,
            facenumber_in_poster INTEGER,
            plot_keywords TEXT,
            movie_imdb_link TEXT,
            num_user_for_reviews INTEGER,
            language TEXT,
            country TEXT,
            content_rating TEXT,
            budget INTEGER,
            title_year INTEGER,
            actor_2_facebook_likes INTEGER,
            imdb_score REAL,
            aspect_ratio REAL,
            movie_facebook_likes INTEGER
        )

    """
    )

    # Import CSV to table
    with open("data/movie_metadata.csv", "r") as movieData:
        csvreader = csv.reader(movieData)
        next(csvreader)
        for row in csvreader:

            cursor.execute(
                """
            INSERT INTO MOVIE (
                color,
                director_name,
                num_critic_for_reviews,
                duration,
                director_facebook_likes,
                actor_3_facebook_likes,
                actor_2_name,
                actor_1_facebook_likes,
                gross,
                genres,
                actor_1_name,
                movie_title,
                num_voted_users,
                cast_total_facebook_likes,
                actor_3_name,
                facenumber_in_poster,
                plot_keywords,
                movie_imdb_link,
                num_user_for_reviews,
                language,
                country,
                content_rating,
                budget,
                title_year,
                actor_2_facebook_likes,
                imdb_score,
                aspect_ratio,
                movie_facebook_likes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

            """,
                row,
            )

    # Write a query and execute it with cursor
    query = "SELECT movie_title FROM MOVIE LIMIT 5"
    cursor.execute(query)

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
