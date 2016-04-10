from Classes.Movie import Movie
from Classes.User import User
from Classes.ReviewData import ReviewData
from ProcessData import ProcessData
from Classes.Logic import Logic


class Main():

    """Main Constructor"""
    def __init__(self):
        pd = ProcessData()
        deli_with_line = '|'
        deli_with_tabs = '\t'
        encoding_latin = 'latin_1'

        self.movie_dict = pd.read_file_return_dict('u.item',
                                                   encoding_latin, deli_with_line)
        self.movie_dict = pd.create_init_inst_of_rows(self.movie_dict, Movie)

        self.user_dict = pd.read_file_return_dict('u.user',
                                                  encoding_latin, deli_with_line)
        self.user_dict = pd.create_init_inst_of_rows(self.user_dict, User)

        #file rows are  user id | movie id | rating | timestamp
        self.review_list = pd.read_file_return_list('u.data',
                                                    encoding_latin, deli_with_tabs)

    def Main(self):

        main = True
        self.process_ratings()
        print(self.movie_dict[1].get_movie_average_score)
        exit()



    def process_ratings(self):
        for row in self.review_list:
            print(self.movie_dict[row[1]].add_ratings(row[0], row[2]))


    def prompt_user(self):
        print("Find a movie rating by id")
        return input(">>>")



if __name__ == '__main__':
    f = Main()
    f.Main()
    #print(f.find_movie_by_id(123))

    #f.main()
