from Classes.Movie import Movie
from Classes.User import User
from Classes.ReviewData import ReviewData
from ProcessData import ProcessData
from Classes.Logic import Logic
from CustomExceptions.StandardClassExemptions import MovieNotFound
from operator import itemgetter


class Main():

    """Main Constructor"""
    def __init__(self):
        pd = ProcessData()
        deli_with_line = '|'
        deli_with_tabs = '\t'
        encoding_latin = 'latin_1'

        #Reads the movie information from files and then creates instances of each item
        self.movie_dict = pd.read_file_return_dict('u.item',
                                                   encoding_latin, deli_with_line)
        self.movie_dict = pd.create_init_inst_of_rows(self.movie_dict, Movie)

        # Reads the user information from files and then creates instances of each item
        self.user_dict = pd.read_file_return_dict('u.user',
                                                  encoding_latin, deli_with_line)
        self.user_dict = pd.create_init_inst_of_rows(self.user_dict, User)

        #file rows are  user id | movie id | rating | timestamp
        self.review_list = pd.read_file_return_list('u.data',
                                                    encoding_latin, deli_with_tabs)
        #takes the user review data and processes it into the classes
        self.process_ratings()

        #set up a dict of the movies containing
        #movie_id : [num_of_reviews, mean_score, user_id_list]
        self.movie_review_list = []

        self.top_ten_rating = []

    def Main(self):

        main = True
        self.set_movie_review_dict()
        self.set_top_ten_movies()
        print(self.get_top_ten_movies())
        exit()



    def process_ratings(self):
        for row in self.review_list:
            if self.movie_dict[row[1]] and self.user_dict[row[0]]:
                self.movie_dict[row[1]].add_ratings_to_dict(row[0], row[2])
                self.user_dict[row[0]].add_to_user_rating_dict(row[1], row[2])
            else:
                raise MovieNotFound("Movie ID {} was entered but not found".format())
            pass


    def prompt_user(self):
        print("Find a movie rating by id")
        return input(">>>")



    """Returns the top X movies by average rating with their
    rating."""
    def get_top_ten_movies(self):
        for row in self.top_ten_rating[:10]:
            print(self.movie_dict[row[1]].get_movie_title())

    def set_top_ten_movies(self):
        self.top_ten_rating = (sorted(self.movie_review_list,
                                      key=itemgetter(1, 2), reverse = True))


    """Compiles a dict of user reviews containing:
        movie_id: [num_of_reviews, average_score, [users_id]]"""
    def set_movie_review_dict(self):
        for row in self.movie_dict:
            #parameters for reviews dict for readability
            num_of_reviews = self.movie_dict[row].get_num_of_reviews()
            mean_score = self.movie_dict[row].get_movie_mean_score()
            #user_id_list = self.movie_dict[row].get_list_users_who_reviewed()
            temp_row = (row, num_of_reviews, mean_score)

            #put this new row into the dict
            self.movie_review_list.append(temp_row)

    def prune_list(self):
        for row in self.movie_review_list:
            pass


    """find the top X movies by average rating that a
    specific
    user has not rated."""
    def get_top_ten_for_user_who_has_not_rated(self):
        pass


if __name__ == '__main__':
    f = Main()
    f.Main()

    #print(f.find_movie_by_id(123))

    #f.main()

#########################################################################################
#                                      Old Code
#########################################################################################
#
# """Returns the average/mean rating for a specific movie"""
#
#
# def get_mean_rating_for_movie(self, a_movie_id):
#     return self.movie_dict[a_movie_id].get_movie_mean_score()
#
#
# """Returns all of the movie reviews in a dict"""
#
#
# def get_all_movie_ratings(self, a_movie_id):
#     return self.movie_dict[a_movie_id].get_all_reviews()
#
#
# def get_num_of_movie_reviews(self, a_movie_id):
#     return self.movie_dict[a_movie_id].get_num_of_reviews()