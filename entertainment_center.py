import fresh_tomatoes
import media   #importing from other file in same folder (Movie Trailer Project)

#the next six variables are instances of the class "Movie" from media.py
#each of which represent the title, storyline, url for their poster image
#as well as a link to their youtube trailer. When run, this file will create
#an html document alongside media.py and fresh tomatoes.py that will display the name and 
#movie poster for each movie listed below. If the image for a particular movie is clicked,
#it will begin playing the youtube movie trailer for that film. 

toy_story = media.Movie("Toy Story",
                        "Movie about a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

burn_after_reading = media.Movie("Burn After Reading",
                                 "Memoirs are stolen by idiots who think they are gov't secrets.",
                                 "https://upload.wikimedia.org/wikipedia/en/4/42/Burn_After_Reading.png",
                                 "https://www.youtube.com/watch?v=SVCHSiRWjJM")

o_brother = media.Movie("O'Brother Where Art Thou",
                        "Three men break out of the chain gang and hilarity ensues",
                        "https://upload.wikimedia.org/wikipedia/en/5/5b/O_brother_where_art_thou_ver1.jpg",
                        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

shaun_of_the_dead = media.Movie("Shaun of the Dead",
                               "Two idiots bumble through a zombie apocolypse.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/e"
                                "/ec/Shaun-of-the-dead.jpg/220px-Shaun-of-the-dead.jpg",
                                "https://www.youtube.com/watch?v=LIfcaZ4pC-4")
                                
fargo = media.Movie("Fargo",
                    "A husband's plan to profit goes terribly wrong.",
                    "https://upload.wikimedia.org/wikipedia/en/3/33/Fargo_%281996_movie_poster%29.jpg",
                    "https://www.youtube.com/watch?v=h2tY82z3xXU")

                    


movies = [toy_story, avatar, burn_after_reading, o_brother, shaun_of_the_dead, fargo]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__name__)
