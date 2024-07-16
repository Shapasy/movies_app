MOVIE_TABLE = \
"""
CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    director TEXT,
    release_year INTEGER,
    length INTEGER,
    PRIMARY KEY (title, director),
    FOREIGN KEY (director) REFERENCES people (name)
)
"""
