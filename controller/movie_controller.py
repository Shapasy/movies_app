from controller.controller import Controller
from views.people_view import PeopleView
from views.movie_view import MovieView


class MovieController(Controller):
    def __init__(self):
        super().__init__()
        self.movie_view = MovieView()
        self.people_view = PeopleView()

    def _is_person_does_not_exist(self, name): # not clean to name the checker method with negative.
        return not self.people_view.is_person_exist(name)

    def _get_length_in_minutes(self, length_str):
        return int(length_str.split(":")[0]) * 60 + int(length_str.split(":")[1])

    def _is_length_not_in_correct_formate(self, length_str): # not clean to name the checker method with negative.
        try:
            self._get_length_in_minutes(length_str)
            return False
        except IndexError:
            return True

    def add_movie(self):
        title = self.handle_input(
            input_message = "Title: "
        )

        length_str = self.handle_input(
            input_message = "Length: ",
            error_message= "Length must be in hh:mm format, try again",
            error_condation_method= self._is_length_not_in_correct_formate
        )
        length = self._get_length_in_minutes(length_str)

        director = self.handle_input(
            input_message = "Director: ",
            error_message= "Director does not exist, try again",
            error_condation_method= self._is_person_does_not_exist
        )

        release_year = self.handle_input(
            input_message = "Release Year: ",
            error_message= "Release year must be a number, try again",
            error_condation_method= self._is_not_number
        )

        actors = []
        while True:
            actor = input("Starring: ").strip()
            if actor == "exit":
                break
            if self._is_person_does_not_exist(actor):
                print("Actor does not exist, try again")
            else:
                actors.append(actor)

        self.movie_view.add_movie(
            title=title,
            director=director,
            release_year=release_year,
            length=length,
            actors=actors
        )

    def _format_length(self, minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours:02}:{minutes:02}"

    def get_movies(self, is_with_actors=False, title_filter=None, director_filter=None, actor_filter=None, order_by_length=None):
        data = self.movie_view.get_movies(
            is_with_actors=is_with_actors,
            title_filter=title_filter,
            director_filter=director_filter,
            actor_filter=actor_filter,
            order_by_length=order_by_length
        )

        for row in data:
            title, director, year, length = row['movie']
            actors = row['actors'] if 'actors' in row else []
            print(f"{title} by {director} in {year}, {self._format_length(length)}")
            if is_with_actors and actors:
                print("Starring:")
                for actor in actors:
                    print(f"    - {actor['name']} at age {actor['age']}")
