import csv

# Creates the database schema and imports data from the CSV file.


def create_and_populate_db(conn):
    cursor = conn.cursor()
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
            row = [
                col.replace("\xa0", " ").strip() if isinstance(col, str) else col
                for col in row
            ]

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
            # print(f"INSERT INTO MOVIE VALUES {tuple(row)};")

    conn.commit()
