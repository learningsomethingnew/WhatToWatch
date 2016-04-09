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

from CustomExceptions.StandardClassExemptions import UserAlreadyReviewed

class Movie():

    def __init__(self, *args):
        self.movie_id = args[0][0]
        self.movie_title = args[0][1]
        self.movie_release_date = args[0][2]
        self.imdb_link = args[0][4]

        #see not at top for genre order
        self.genre_list = args[0][5:]

        #For any movie rating by users.
        # user id | rating
        self.movie_rating = {}

    def add_ratings(self, a_user_id, a_rating):
        if a_user_id in self.movie_rating:
            raise UserAlreadyReviewed
        else:
            self.movie_rating[a_user_id] = a_rating


    def get_movie_average_score(self):
        return sum(self.movie_rating.values()/len(self.movie_rating))





