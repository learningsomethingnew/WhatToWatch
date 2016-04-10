################################################
# Processes data from files.
#  ready from return dict/list -  Assumes working in movie data dir
################################################


from SupportClasses.CreateFiles.csv_files import open_csv_return_giant_list


class ProcessData():
    def __init__(self):
        # Setting up dirs for future reference
        self._saved_classes_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/SavedClassesData'
        self._movie_data_dir = '/Users/Nic/TIY/W2/WhatToWatch/Data/MovieLensData/ml100k'

    """Takes the file name and feeds the information
        into the appropriate class. Returns dict"""

    def read_file_return_dict(self, a_file, a_encode, deli_type):
        temp_name = self._movie_data_dir + '/' + a_file
        temp_dict = {}
        # print(temp_name)
        a = open_csv_return_giant_list(temp_name, a_encode, deli_type)
        #print("Length = {}".format(len(a)))
        for row in a:
            temp_dict[row[0]] = row
        #print(temp_dict)
        return {int(row[0]): row for row in a}

    """reads in a file and returns a list of its contents.
        Requires the filename,
        encoding, and delimiter type"""

    def read_file_return_list(self, a_file, a_encode, deli_type):
        temp_name = self._movie_data_dir + '/' + a_file
        temp_list = []
        a = open_csv_return_giant_list(temp_name, a_encode, deli_type)
        for i, row in enumerate(a):
            print(i, row)



    """Takes the data that is read from file and creates
        instances of the data."""
    def create_init_inst_of_rows(self, a_data_type, a_class):
        temp_dict = {}
        if type(a_data_type) == dict:
            temp_val = 0
            for key in a_data_type:
                temp_dict[key] = a_class(a_data_type[key])
            return (temp_dict)



            # elif type(a_data_type) == list:
            # return a_class(a_row)

if __name__ == '__main__':
    f = ProcessData()
    # f.read_file('u.item', Movie)

    # f.main()



#########################################################################################
#                                      Old Code
#########################################################################################

