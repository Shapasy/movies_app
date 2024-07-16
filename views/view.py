class View:
    def __init__(self, database_connection):
        self.database_connection = database_connection
        self.database_cursor = self.database_connection.cursor()
