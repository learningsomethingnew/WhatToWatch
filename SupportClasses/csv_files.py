import csv


"""Open CSV that has tabs and return dictionary"""
def open_csv_return_dict(a_file_name):
    with open(a_file_name, encoding='latin_1') as f:
        reader = csv.DictReader(f, delimiter='|')# fieldnames = ['movie_id','title'])
        #temp_dict = {}
        for row in reader:
            print(row)
            #temp_dict = row
        #return temp_dict

"""Open CSV files and returns a giant list"""
def open_csv_return_giant_list(a_file_name, a_enconding, a_delimeter):
    with open(a_file_name, encoding=a_enconding) as f:  # automatically closes the file when done
        temp_list = []
        reader = csv.reader(f, delimiter = a_delimeter)
        # Reads and appends the heads of csv
        temp_list.append(next(reader))
        # print(temp_list)
        # print('------')
        for row in reader:
            # print(row)
            temp_list.append(row)
        return temp_list


"""Open CSV files and returns list row by row"""
def open_csv__return_list_by_row(a_file_name):
    with open(a_file_name) as f:  # automatically closes the file when done
        temp_list = []
        reader = csv.reader(f, skipinitialspace=True)
        # Reads and appends the heads of csv
        next(reader)
        print(temp_list)
        for row in reader:
            # print(row)
            return (row)


