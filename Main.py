from Classes.Movie import Movie
from Classes.User import User
from Classes.ReviewData import ReviewData
from ProcessData import ProcessData


class Main():

    """Main Constructor"""
    def __init__(self):
        pd = ProcessData()
        deli_with_line = '|'
        deli_with_tabs = '\t'
        encoding_latin = 'latin_1'
        self.movie_dict = pd.read_file('u.item', Movie,
                                       encoding_latin, deli_with_line)
        self.user_dict = pd.read_file('u.user', User,
                                      encoding_latin, deli_with_line)

        #file rows are  user id | item id | rating | timestamp
        #self.review_dict = pd.read_file('u.data', ReviewData,
                                        #encoding_latin, deli_with_tabs)

        print(self.movie_dict)

    def main(self):


        main = True
        while main == True:
            pass


    def find_all_ratings_for_movie_by_id(self, a_movie_id):
        return


    def test_if_ratings_exist_for_movie_by_id(self, an_id):
        pass

    def prompt_user(self):
        print("Find a movie rating by id")
        return input(">>>")



if __name__ == '__main__':
    f = Main()
    #print(f.find_movie_by_id(123))

    #f.main()
