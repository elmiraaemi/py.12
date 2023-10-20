from Media import Media
class Film(Media):
    def __init__(self, name, director, IMDB, url, duration, casts, typ, year, ganer):
        super().__init__(name, director, IMDB, url, duration, casts, typ, year)
        self.ganer = ganer