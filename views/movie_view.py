import sqlite3
from views.view import View


class MovieView(View):
    def __init__(self, database_connection) -> None:
        super().__init__(database_connection)

    def is_director(self, name):
        self.database_cursor.execute(
            "SELECT director FROM movies WHERE director = ? LIMIT 1",
            (name,)
        )
        return bool(self.database_cursor.fetchone())

    def add_movie(self, title, director, release_year, length, actors):
        try:
            self.database_cursor.execute(
                "INSERT INTO movies (title, director, release_year, length) VALUES (?, ?, ?, ?)",
                (title, director, release_year, length,)
            )
            for actor in actors:
                self.database_cursor.execute(
                    "INSERT INTO movie_actors (movie_title, movie_director, actor_name) VALUES (?, ?, ?)",
                    (title, director, actor,)
                )
            self.database_connection.commit()
            print(f"Added movie {title} by {director} in {release_year}")
        except sqlite3.IntegrityError as ex:
            # it is better to raise custom exceptions here, and then handle it inside controller, it increases code flexibility
            print(f"Failed to add movie: {ex}")
            return

    def get_movies(self, is_with_actors=False, title_filter=None, director_filter=None, actor_filter=None, order_by_length=None):
        query = "SELECT title, director, release_year, length FROM movies"

        filters = []
        if title_filter:
            filters.append(f"title like  '{title_filter}'")
        if director_filter:
            filters.append(f"director like  '{director_filter}'")
        if actor_filter:
            query += " JOIN movie_actors ON movies.title = movie_actors.movie_title AND movies.director = movie_actors.movie_director"
            filters.append(f"actor_name like  '{actor_filter}'")
        if filters:
            query += " WHERE " + " AND ".join(filters)

        if order_by_length == 'asc':
            query += " ORDER BY title ASC"
        elif order_by_length == 'desc':
            query += " ORDER BY title DESC"

        self.database_cursor.execute(query)
        movies = self.database_cursor.fetchall()

        results = [{'movie': movie} for movie in movies]

        if is_with_actors:
            for result in results:
                title, director, year, _ = result['movie']
                self.database_cursor.execute(
                    "SELECT actor_name, birth_year FROM movie_actors JOIN people ON movie_actors.actor_name = people.name WHERE movie_title = ? AND movie_director = ?",
                    (title, director,)
                )
                actors = self.database_cursor.fetchall()
                result['actors'] = tuple([{'name' : name, 'age': year-birth_year}  for name, birth_year in actors])

        return results
