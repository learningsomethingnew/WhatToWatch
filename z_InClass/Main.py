from SupportClasses.FileActions import FileActions
from z_InClass.StockData import StockData


class Main():

    def __init__(self):
        self.a_file_name = 'EOD-GOOG.csv'

        self.f = FileActions()

        self._list_of_stock_instances = []

    def create_instance_of_data(self):

        a_giant_list = self.f.open_csv__return_giant_list(self.a_file_name)

        for row in enumerate(a_giant_list):
            string_name = "end_of_day_row{}".format(row[0])
            row[1].insert(0, string_name)
            #print(row)
            string_name = StockData(row[1])
            self._list_of_stock_instances.append(string_name)
        self.read_list(self._list_of_stock_instances)

    def read_list(self, aList):
        for i, row in enumerate(aList):
            print(aList[i])

if __name__ == '__main__':
    f = Main()
    f.create_instance_of_data()


