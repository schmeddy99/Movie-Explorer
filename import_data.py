import csv

# Handles importing the CSV and inserting rows


def populate_db(conn):
    cursor = conn.cursor()
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
