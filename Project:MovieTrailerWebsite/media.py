import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ['G', 'PG', 'PG-13','R']

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # this is constructor in python. __ underscores on both sides mean init word is reserved in python.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):     # this is an instance method
        webbrowser.open(self.trailer_youtube_url)