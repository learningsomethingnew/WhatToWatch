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

from CustomExceptions.StandardClassExemptions import UserAlreadyReviewed, NoneWasPassed

class Movie():

    def __init__(self, *args):
        #print(args)

        self.movie_id = args[0][0]
        self.movie_title = args[0][1]
        self.movie_release_date = args[0][2]
        self.imdb_link = args[0][4]

        #see not at top for genre order
        self.genre_list = args[0][5:]

        #For any movie rating by users.
        # user id | rating
        self.movie_rating = {}
        self.mean_score = 0
        self.number_of_reviews = 0

    """Adds to the movie_rating dict for processing specific movie data"""
    def add_ratings_to_dict(self, a_user_id, a_rating):
        if a_user_id in self.movie_rating:
            raise UserAlreadyReviewed("Movie class: add rating: "
                                      "user {} already reviewed {}"
                                      .format(a_user_id, a_rating))

        elif a_user_id == None or a_rating == None:
            raise NoneWasPassed("Movie class: add rating: "
                                "user {} passed a none"
                                .format(a_user_id, a_rating))
        else:
            self.movie_rating[a_user_id] = a_rating
            self.number_of_reviews = len(self.movie_rating)
            self.mean_score = sum(self.movie_rating.values())/self.number_of_reviews
            # print("User {} gave score of {}".format(a_user_id, a_rating))
            #print("Movie Rating Length {}".format(len(self.movie_rating)))

    """Returns the mean score"""
    def get_movie_mean_score(self):
        return self.mean_score

    """Returns all of the reviews as a dict"""
    def get_dict_all_reviews(self):
        return self.movie_rating

    def get_list_users_who_reviewed(self):
        return list(self.movie_rating.keys())

    def get_list_user_scores(self):
        return list(self.movie_rating.values())

    """Returns the len of movie reviews"""
    def get_num_of_reviews(self):
        return self.number_of_reviews

    def get_movie_title(self):
        return self.movie_title





