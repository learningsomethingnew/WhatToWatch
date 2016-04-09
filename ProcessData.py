from SupportClasses.CreateFiles.csv_files import open_csv_return_giant_list


class ProcessData():

    def __init__(self):
        # Setting up dirs for future reference
        self._movie_data_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/MovieLensData/ml100k'
        self._saved_classes_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/SavedClassesData'

    """Takes the file name and feeds the information
        into the appropriate class. Returns dict"""
    def read_file(self, a_file, a_class, a_encode, deli_type):
        temp_name = self._movie_data_dir+'/'+a_file
        temp_dict = {}
        #print(temp_name)
        a = open_csv_return_giant_list(temp_name, a_encode, deli_type)
        #print(len(a))
        for row in a:
            #self.create_initial_instances(row, a_class)
            temp_dict[row[0]] = a_class(row)
        print(temp_dict)
        return temp_dict

    """Takes the data that is read from file and creates
        instances of the data."""
    def create_initial_instances(self, a_row, a_class):
        return a_class(a_row)


if __name__ == '__main__':
    f = ProcessData()
    #f.read_file('u.item', Movie)

    #f.main()
