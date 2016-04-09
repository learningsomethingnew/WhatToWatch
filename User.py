####################################
# Holds the user generic user data #
####################################


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

    def add_to_user_rating_dict(self, user_rating, movie_score):
        pass

    def __str__(self):
        print("UserID {} {} {} ".format(self.user_id, self.age, self.gender))

class WrongType(Exception):
    pass



