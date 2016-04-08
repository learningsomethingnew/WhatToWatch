##########################
# Holds the user generic
# user data
##########################


class User():

    def __init__(self, *args):
        self.user_id = args[0][0]
        self.age = args[0][1]
        self.gender = args[0][2]
        self.occupation = args[0][3]
        self.zip_code = self.test_zip_code(args[0][4])


    """Testing for non ints in the zip"""
    def test_zip_code(self, a_item):
        try:
            int(a_item)
            print("Good Zip{}".format(a_item))
            return a_item
        except:
            print("Bad Zip")
            return 00000

