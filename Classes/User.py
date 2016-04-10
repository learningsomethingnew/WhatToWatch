####################################
# Holds the user generic user data #
####################################

from CustomExceptions.StandardClassExemptions import WrongType, UserAlreadyReviewed

class User():

    def __init__(self, *args):
        self.user_id =self.convert_to_int(args[0][0])
        self.age = self.convert_to_int(args[0][1])
        self.gender = args[0][2]
        self.occupation = args[0][3]
        self.zip_code = self.test_zip_code(args[0][4])

        #user rating stores dict of movie_id | movie_score
        self.user_rating = {}

    """Testing for non ints in the zip.
        If one is found, sets zip to 00000"""
    def test_zip_code(self, a_item):
        try:
            int(a_item)
            return a_item
        except:
            return 00000

    def convert_to_int(self, a_item):
        try:
            return int(a_item)
        except:
            raise WrongType("Converting to int was passed a non-int")

    def add_to_user_rating_dict(self, a_movie_id, a_movie_score):
        if a_movie_id in self.user_rating:
            raise UserAlreadyReviewed
        else:
            self.user_rating[a_movie_id] = a_movie_score

    """Returns a dict of instance user reviews
        movie_id | movie_score"""
    def get_all_user_reviews(self):
        return self.user_rating

    def __str__(self):
        return("UserID: {}, Age: {}, Gender:{} ".format(self.user_id, self.age, self.gender))





