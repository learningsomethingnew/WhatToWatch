

class Logic():

    def __init__(self):
        pass

    def find_movie_by_id(self, a_id):
        search_list = []
        for object in self._movie_list:
            search_list.append((object.movie_id, object.movie_title))
        return search_list[(a_id)][1]