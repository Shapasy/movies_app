import re
from database.database_handler import database_handler
from controller.people_controller import PeopleController
from controller.movie_controller import MovieController


def connect_to_db():
    try:
        database_handler.connect()
        database_handler.create_tables()
        print("Connected to the database successfully")
        return database_handler.connection
    except ConnectionError:
        print("Failed to connect to database")
        return

if __name__ == "__main__":
    connect_to_db()

    people_controller = PeopleController()
    movie_controller = MovieController()

    while True: # handling commands (The User Interface)
        command = input(">> ")
        command = command.strip()

        if command.startswith("a -p"):
            people_controller.add_person()

        elif command.startswith("a -m"):
            movie_controller.add_movie()

        elif command.startswith("l"):   # pagination is important to improve the latency.
            is_with_actors = "-v" in command
            title_filter = None
            director_filter = None
            actor_filter = None
            order_by_length = None

            match = re.search(r'-t "([^"]+)"', command)
            if match:
                title_filter = match.group(1)

            match = re.search(r'-d "([^"]+)"', command)
            if match:
                director_filter = match.group(1)

            match = re.search(r'-a "([^"]+)"', command)
            if match:
                actor_filter = match.group(1)

            if "-la" in command:
                order_by_length = 'asc'
            elif "-ld" in command:
                order_by_length = 'desc'

            movie_controller.get_movies(
                is_with_actors=is_with_actors,
                title_filter=title_filter,
                director_filter=director_filter,
                actor_filter=actor_filter,
                order_by_length=order_by_length
            )

        elif command.startswith("d -p"):
            people_controller.delete_person()

        else:
            print('Wrong command, try again')
