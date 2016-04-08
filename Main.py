from ProcessData import ProcessData
from Movie import Movie
from User import User


class Main():

    """Main Constructor"""
    def __init__(self):
        pd = ProcessData()
        self.movie_list = pd.read_file('u.item', Movie)
        self.user_list = pd.read_file('u.user', User)


    def main(self):


        main = True
        while main == True:
            pass



    def prompt_user(self):
        print("Find a movie rating by id")
        return input(">>>")



if __name__ == '__main__':
    f = Main()
    #print(f.find_movie_by_id(123))

    #f.main()
