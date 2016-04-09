

class ReviewData():

    def __init__(self, *args):
        self.user_id = args[0][0]
        self.item_id = args[0][1]
        self.movie_rating = args[0][2]
        self.meta_data = args[0][3:]