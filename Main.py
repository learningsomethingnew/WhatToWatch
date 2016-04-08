from SupportClasses.csv_files import open_csv_return_giant_list
from Movies import Movies


class Main():

    """Main Constructor"""
    def __init__(self):
        #Setting up dirs for future reference
        self._movie_data_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/MovieLensData/ml100k'
        self._saved_classes_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/SavedClassesData'
        self._movie_data = 'u.item'
        self._enconding = 'latin_1'
        self._movie_list = []

    def main(self):
        main = True

        while main == True:
            a = self.prompt_user()



    #read in files
    def read_file(self, a_file):
        temp_name = self._movie_data_dir+'/'+a_file
        print(temp_name)
        a = open_csv_return_giant_list(temp_name, self._enconding)
        print(len(a))
        for row in a:
            print(row[0])
            self.create_initial_instances(row)

    def create_initial_instances(self, a_row):
        temp_name = 'movie_id_{}'.format(a_row[0])
        temp_name = Movies(a_row)
        self._movie_list.append(temp_name)

    def prompt_user(self):
        print("Find a movie rating by id")
        return input(">>>")

    def read_list(self, a_list):
        for i, row in enumerate(a_list):
            print(a_list[i][0])

if __name__ == '__main__':
    f = Main()
    f.read_file('u.item')
    f.read_list(f._movie_list)

    #f.main()