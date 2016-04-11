##############################################################
# File last modified on: 04/10/2016
#Sorts top movies list by
# num of reviews and then average rating.
##############################################################
from operator import itemgetter


class GetPopMovies(): 

    def __init__(self, a_compiled_movie_reviews):
        self.a_list = a_compiled_movie_reviews
        self.set_list_top_movies_by_popularity()

    """Sorts top movies list by
        num of reviews and then average rating.
        [(movie_id, num_of_reviews, average_score)]"""

    def set_list_top_movies_by_popularity(self):
        self.list_top_movies_by_popularity = (
            sorted(self.a_list,
                   key=itemgetter(1, 2), reverse=True))

    """Returns the sorted top 10 movies by
    num of reviews and then average rating."""

    def get_top_ten_movies_by_popularity(self):
        temp_list = []
        for row in self.list_top_movies_by_popularity:
            return(self.movie_dict[row[1]].get_movie_title())






if __name__ == '__main__':
    f = GetPopMovies()
#########################################################################################
,#                                      Old Code
#########################################################################################
