import sqlite3
from views.view import View


class PeopleView(View):
    def is_person_exist(self, name):
        self.db_cursor.execute(
            "SELECT name FROM people WHERE name = ? LIMIT 1",
            (name,)
        )
        return bool(self.db_cursor.fetchone())

    def add_person(self, name, birth_year):
        try:
            self.db_connection.execute(
                "INSERT INTO people (name, birth_year) VALUES (?, ?)",
                (name, birth_year,)
            )
            self.db_connection.commit()
            print(f"Added person {name} born in {birth_year}")
        except sqlite3.Error as ex:
            # it is better to raise custom exceptions here, and then handle it inside controller, it increases code flexibility
            print(f"Failed to add person: {ex}")
            return

    def delete_person(self, name):
        try:
            self.db_cursor.execute(
                "DELETE FROM movie_actors WHERE actor_name = ?",
                (name,)
            )
            self.db_cursor.execute(
                "DELETE FROM people WHERE name = ?",
                (name,)
            )
            self.db_connection.commit()
            print(f"Deleted person {name} from the database")
        except sqlite3.Error as ex:
            # it is better to raise custom exceptions here, and then handle it inside controller, it increases code flexibility
            print(f"Failed to delete person: {ex}")
            return
