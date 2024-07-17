from database.database_handler import database_handler


class View:
    def __init__(self):
        if not database_handler.connection:
            raise ConnectionError(
                "Can not initiate a View without establishing a database connection"
        )
        self.db_connection = database_handler.connection
        self.db_cursor = self.db_connection.cursor()
