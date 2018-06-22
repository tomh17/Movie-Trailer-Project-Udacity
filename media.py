import webbrowser


class Movie():
    """This class provides a way to store information."""

# will show up as the __name__ variable ^

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
# example of a class variable
# all instances of class "Movie"
# contain these ratings

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        # def __init__ initializes the
        # class movie and allows you to define
        # attributes of the class for each
        # instance created of that class (ie.
        # each movie will have different attributes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # a method that will open the youtube
        # trailer for a specified movie
        webbrowser.open(self.trailer_youtube_url)
