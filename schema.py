import sqlite3

# Contains all CREATE TABLE statements


def create_movie_table(conn):
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
