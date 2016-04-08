##########################
# Holds the user generic
# user data
##########################


class Users():

    def __init__(self, *args):
        self.user_id = args[0][0]
        self.age = args[0][1]
        self.gender = args[0][2]
        self.occupation = args[0][3]
        self.zip_code = args[0][4]

