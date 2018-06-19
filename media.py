import webbrowser

class Movie():
    """This class proivides a way to store information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
#toystory = Movie()

#toystory.title = "Toy Story"
#print(toystory.title)
