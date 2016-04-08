#######################################################
# takes in a list of information as args
# and parses the variables in it.
#
#  Genre Information about the list
#   unknown | Action | Adventure | Animation |
#   Children's | Comedy | Crime | Documentary |
#   Drama | Fantasy | Film - Noir | Horror |
#   Musical | Mystery | Romance | Sci - Fi |
#   Thriller | War | Western |
#######################################################

class Movie():

    def __init__(self, *args):
        self.movie_id = args[0][0]
        self.movie_title = args[0][1]
        self.movie_release_date = args[0][2]
        self.imdb_link = args[0][4]
        self.genre_list = args[0][5:]





