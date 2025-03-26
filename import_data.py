import csv
import utils

# Handles importing the CSV and inserting rows


def populate_normalized_db(conn):
    cursor = conn.cursor()

    with open("data/movie_metadata.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean string fields
            clean = lambda s: (
                s.replace("\xa0", " ").strip() if isinstance(s, str) else s
            )

            director_name = clean(row["director_name"])
            director_likes = int(row["director_facebook_likes"] or 0)
            director_id = utils.get_or_create_director(
                conn, director_name, director_likes
            )

            # Insert movie
            cursor.execute(
                """
                INSERT INTO movies (
                    title, year, imdb_score, gross, duration, budget,
                    content_rating, country, language, color, director_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    clean(row["movie_title"]),
                    int(row["title_year"] or 0),
                    float(row["imdb_score"] or 0),
                    int(row["gross"] or 0),
                    int(row["duration"] or 0),
                    int(row["budget"] or 0),
                    clean(row["content_rating"]),
                    clean(row["country"]),
                    clean(row["language"]),
                    clean(row["color"]),
                    director_id,
                ),
            )
            movie_id = cursor.lastrowid

            # Insert actors
            for i in range(1, 4):
                actor_name = clean(row[f"actor_{i}_name"])
                actor_likes = int(row.get(f"actor_{i}_facebook_likes") or 0)
                if actor_name:
                    actor_id = utils.get_or_create_actor(conn, actor_name, actor_likes)
                    cursor.execute(
                        "INSERT INTO movie_actors (movie_id, actor_id, role_order) VALUES (?, ?, ?)",
                        (movie_id, actor_id, i),
                    )

            # Insert genres
            genre_string = clean(row["genres"])
            if genre_string:
                genres = [g.strip() for g in genre_string.split("|") if g.strip()]
                for genre_name in genres:
                    genre_id = utils.get_or_create_genre(conn, genre_name)
                    cursor.execute(
                        "INSERT INTO movie_genres (movie_id, genre_id) VALUES (?, ?)",
                        (movie_id, genre_id),
                    )

    conn.commit()
