import queries.queries as queries
import queries.fun_queries as discover
import utils


def search_menu(conn):
    while True:
        search_choice = input(
            "Choose an option:\n "
            "1. Search by title\n "
            "2. Search by director\n "
            "3. Filter by genre\n "
            "4. Filter by year\n "
            "5. Filter by rating\n "
            "6. Exit\n"
            "Command: "
        )
        if search_choice == "1":
            title = input("Enter a movie title to search: ")
            results = queries.search_by_title(conn, title)
            utils.print_results(results)
        elif search_choice == "2":
            director = input("Enter a director to search: ")
            results = queries.search_by_director(conn, director)
            utils.print_results(results)
        elif search_choice == "3":
            genre = input("Enter a genre: ")
            results = queries.search_by_genre(conn, genre)
            utils.print_results(results)
        elif search_choice == "4":
            year = input("Enter a year: ")
            if not year.isdigit():
                print("Please enter a valid year.")
                continue
            results = queries.search_by_year(conn, int(year))
            utils.print_results(results)
        elif search_choice == "5":
            rating = int(input("Enter a minimum rating: "))
            results = queries.search_by_rating_threshold(conn, rating)
            utils.print_results(results)
        elif search_choice == "6":
            break
        else:
            print("Invalid selection. Please try again. ")


def insights_menu(conn):
    while True:
        insights_choice = input(
            "\n--- Movie Insights ---\n"
            "a. Top rated movies\n"
            "b. Average rating by genre\n"
            "c. Movies per decade\n"
            "d. Most frequent director\n"
            "e. Average gross by country\n"
            "f. Back to main menu\n"
            "Command: "
        )

        if insights_choice == "a":
            limit = input("How many top-rated movies do you want to see? ")
            if not limit.isdigit():
                print("Please enter a valid number.")
                continue
            results = queries.get_top_rated_movies(conn, int(limit))
            utils.print_results(results)

        elif insights_choice == "b":
            results = queries.get_average_rating_by_genre(conn)
            utils.print_results(results)

        elif insights_choice == "c":
            results = queries.get_movies_per_decade(conn)
            utils.print_results(results)

        elif insights_choice == "d":
            results = queries.most_frequent_director(conn)
            utils.print_results(results)

        elif insights_choice == "e":
            results = queries.get_avg_gross_by_country(conn)
            utils.print_results(results)

        elif insights_choice == "f":
            break

        else:
            print("Invalid selection. Please try again.")


def discovery_menu(conn):
    while True:
        discovery_choices = input(
            "\n--- Surprise & Discovery ---\n"
            "a. Surprise me!\n"
            "b. Longest title\n"
            "c. Common genre words\n"
            "d. Word count stats\n"
            "e. Back to main menu\n"
            "Command: "
        )

        if discovery_choices == "a":
            results = discover.get_random_movie(conn)
            utils.print_results(results)

        elif discovery_choices == "b":
            results = discover.get_longest_movie_title(conn)
            utils.print_results(results)

        elif discovery_choices == "c":
            results = discover.get_most_common_genre_word(conn)
            utils.print_results(results)

        elif discovery_choices == "d":
            results = discover.count_words_in_titles(conn)
            utils.print_results(results)

        elif discovery_choices == "e":
            break

        else:
            print("Invalid selection. Please try again.")
