####################################################################
# Library of File methods
# Saving object?
#   Use "save_to_pickle"
####################################################################

from os import path, getcwd
from pickle import dump, load
import csv

"""Class can be init with a dir but if not, it will assume working directory"""
class FileActions():

    def __init__(self, a_dir = None):
        self.a_dir = a_dir
        self.a_dir = self.change_none_dir_to_cwd()

    """If a_dir is == None, sets the dir to current working dir"""
    def change_none_dir_to_cwd(self):
        if self.a_dir == None:
            return getcwd()
        else:
            return self.a_dir

    """Tests to see if a dir exists"""
    def test_if_dir_exists(self):
        return path.isdir(self.a_dir)

    def create_dir(self):
        pass

    def test_if_file_exists(a_file_name):
        return path.isfile()

    """Save file with data in pickle format. Must pass the data to pickle"""
    def save_to_pickle_file(self, a_data, a_file_name):
        dump(a_data, open(a_file_name+".p", "wb"))


    """Open file with data from pickle format to original data"""
    def retrieve_pickled_file(self, a_file_name):
        return load(open(a_file_name+".p", "rb"))

    """Open CSV files and returns a giant list"""
    def open_csv__return_giant_list(self, a_file_name):
        with open(a_file_name) as f:  # automatically closes the file when done
            temp_list = []
            reader = csv.reader(f, skipinitialspace=True)
            #Reads and appends the heads of csv
            temp_list.append(next(reader))
            #print(temp_list)
            #print('------')
            for row in reader:
                #print(row)
                temp_list.append(row)
            return temp_list

    """Open CSV files and returns list row by row"""
    def open_csv__return_list_by_row(self, a_file_name):
        with open(a_file_name) as f:  # automatically closes the file when done
            temp_list = []
            reader = csv.reader(f, skipinitialspace=True)
            #Reads and appends the heads of csv
            next(reader)
            print(temp_list)
            for row in reader:
                # print(row)
                return(row)

    """Open CSV that has tabs and return dictionary"""
    def open_csv_return_dict(self, a_file_name):
        with open(a_file_name) as f:
            reader = csv.DictReader(f, delimiter='|')
            for row in reader:
                print(row)


if __name__ == '__main__':
    f = FileActions()
    print(f.test_if_dir_exists())
    f.open_csv_return_dict('students.csv')
