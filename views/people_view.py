import sqlite3
from views.view import View


class PeopleView(View):
    def __init__(self, database_connection):
        super().__init__(database_connection)

    def is_person_exist(self, name):
        self.database_cursor.execute(
            "SELECT name FROM people WHERE name = ? LIMIT 1",
            (name,)
        )
        return bool(self.database_cursor.fetchone())

    def add_person(self, name, birth_year):
        try:
            self.database_connection.execute(
                "INSERT INTO people (name, birth_year) VALUES (?, ?)",
                (name, birth_year,)
            )
            self.database_connection.commit()
            print(f"Added person {name} born in {birth_year}")
        except sqlite3.Error as ex:
            # it is better to raise custom exceptions here, and then handle it inside controller, it increases code flexibility
            print(f"Failed to add person: {ex}")
            return

    def delete_person(self, name):
        try:
            self.database_cursor.execute(
                "DELETE FROM movie_actors WHERE actor_name = ?",
                (name,)
            )
            self.database_cursor.execute(
                "DELETE FROM people WHERE name = ?",
                (name,)
            )
            self.database_connection.commit()
            print(f"Deleted person {name} from the database")
        except sqlite3.Error as ex:
            # it is better to raise custom exceptions here, and then handle it inside controller, it increases code flexibility
            print(f"Failed to delete person: {ex}")
            return
