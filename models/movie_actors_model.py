# association table
MOVIE_ACTORS_TABLE = \
"""
CREATE TABLE IF NOT EXISTS movie_actors (
    movie_title TEXT,
    movie_director TEXT,
    actor_name TEXT,
    PRIMARY KEY (movie_title, movie_director, actor_name),
    FOREIGN KEY (movie_title, movie_director) REFERENCES movies (title, director),
    FOREIGN KEY (actor_name) REFERENCES people (name)
)
"""
