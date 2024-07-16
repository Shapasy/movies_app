import configparser
import sqlite3
from models.movie_model import MOVIE_TABLE
from models.people_model import PEOPLE_TABLE
from models.movie_actors_model import MOVIE_ACTORS_TABLE


class DatabaseHandler:
   def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.database_name = config['database']['name']
        self.connection = None

   def connect(self):
    try:
        self.connection = sqlite3.connect(f'{self.database_name}.db')
        return self.connection
    except sqlite3.Error as ex:
        raise ConnectionError(f"Failed to connect to database: {ex}")

   def create_tables(self):
      cursor = self.connection.cursor()
      cursor.execute(MOVIE_TABLE)
      cursor.execute(PEOPLE_TABLE)
      cursor.execute(MOVIE_ACTORS_TABLE)
      self.connection.commit()
