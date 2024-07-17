from database.database_handler import database_handler


class Controller:
    def __init__(self):
        if not database_handler.connection:
            raise ConnectionError(
                "Can not initiate a Controller without establishing a database connection"
            )
        self.db_connection = database_handler.connection

    def handle_input(self, input_message, error_message=None, error_condation_method=None):
        target = None
        is_first_time = True
        while not target or (error_condation_method and error_condation_method(target)):
            if not is_first_time and error_message:
                print(error_message)
            else:
                is_first_time = False
            target = input(input_message).strip()
        return target

    def _is_not_number(self, num_str):  # not clean to name the checker method with negative.
        return not num_str.isnumeric()
