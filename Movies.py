#######################################################
# takes in a list of information as args
# and parses the variables in it.
#######################################################

class Movies():

    def __init__(self, *args):
        print("Movie Instance Here")
        self._movie_id = args[0][0]
        # print(self._name)
        self._movie_title = args[0][1]
        # print(self._date)
        self._open = args[0][2]
        self._high = args[0][3]
        self._low = args[0][4]
        self._close = args[0][5]
        self._volume = args[0][6]