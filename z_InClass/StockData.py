# Read a CSV file in Python containing EOD stock data and
# transform the CSV in to a list of objects, one for each row.✓
#
# Your class must contain at least the Date, Open, High, Low,
# Close, and Volume.✓
#
# If you are doing any complex logic in the class constructor,
# such as parsing a string to a date, you should have unit
# tests for that constructor function.
#
# Using test-driven development, write a method for your class to
# calculate and return the average price between the open,
# high, low, & close.




class StockData():

    def __init__(self, *args):
        print("STOCK_DATA: INPUT FROM MAIN")
        #print(args)
        self._name = args[0][0]
        #print(self._name)
        self._date = args[0][1]
        #print(self._date)
        self._open = args[0][2]
        self._high = args[0][3]
        self._low = args[0][4]
        self._close = args[0][5]
        self._volume = args[0][6]
        #print(self._volume)

    def __str__(self):
        a_string = ("Instance of stock data {} with date of {}".format(self._name, self._date))
        return a_string

