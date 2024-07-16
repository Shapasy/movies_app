from controller.controller import Controller
from views.people_view import PeopleView
from views.movie_view import MovieView


class PeopleController(Controller):
    def __init__(self, db_connection):
        super().__init__(db_connection)
        self.movie_view = MovieView(db_connection)
        self.people_view = PeopleView(db_connection)

    def add_person(self):
        name = self.handle_input(
            input_message = "Name: ",
            error_message= "Person is alreadt exist, try again",
            error_condation_method= self.people_view.is_person_exist
        )
        birth_year = int(self.handle_input(
            input_message="Year of Birth: ",
            error_message= "Year of Birth must be a number, try again",
            error_condation_method= self._is_not_number
        ))
        self.people_view.add_person(name, birth_year)

    def _is_person_deletion_not_valid(self, name):  # not clean to name the checker method with negative.
        if not self.people_view.is_person_exist(name):
            print("Person does not exist, please try again")
            return True
        if self.movie_view.is_director(name):
            print("This is person is a director, please try again")
            return True
        return False

    def delete_person(self):
        name = self.handle_input(
            input_message = "Name: ",
            error_condation_method= self._is_person_deletion_not_valid
        )
        self.people_view.delete_person(name)
