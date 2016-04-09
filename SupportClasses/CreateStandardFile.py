##############################################################
# Last Modified: 4/9
#
# Creates a standard file for consistent beginning of file
# commenting, class name, and starts with the final with
# and init that passes.
#
# Things to add:
#   git recognition
#   Create dir,
#   go up a level,
##############################################################
import os
import glob
import time


class CreateStandardFile():

    def __init__(self):
        self._ignore_dir = ['.git', '.idea', '__pycache__']
        self.support_dir = "/SupportClasses"

        #current dir list
        self._dir_list = []

        #Kick of any methods to set up structure
        self._root_dir = self.set_main_dir()
        self.filename = []
        self.file_time = "# File last modified on: {}".format(time.strftime("%m/%d/%Y"))

        ########################################
        self.python_file_list = ["##############################################################\n",

                                 self.file_time,
                                 "\n"
                                 '# Please define the class here\n',
                                 "##############################################################\n",
                                 "\n\n\n"]


    """Globs the dir set by a_dir. Stores in a temp_list
        sends to test method to remove unwanted dirs.
        The return from test method sets the _dir_list"""
    def find_dirs_in_cwd(self, a_dir):
        temp_list = []
        for name in glob.glob(a_dir+"/*/"):
            temp_list.append(name)
        self._dir_list = self.test_for_ignored_dir(temp_list)
        self._dir_list = sorted(self._dir_list)
        #inserting current working dir as a save options
        self._dir_list.insert(0, self._root_dir)


    """Takes in a list dir, compares the input against a
        of defined ignored dirs, and returns the difference"""
    def test_for_ignored_dir(self, a_dir_list):
        return(list(set(a_dir_list)-
                          {i for e in self._ignore_dir
                           for i in a_dir_list if e in i}))

    """Prints the menu for the user to select dirs from"""
    def menu(self):
        print("Which dir would you like to save the file too?")
        print("----------------------------------------------")
        self.print_dirs()
        print("type q to quit")
        print('\n')

    """removes the upper dirs from the strings before printing"""
    def print_dirs(self):
        slash_index = self._root_dir.rfind('/')
        temp_num = 1
        for a_dir in self._dir_list:
            print("{}: {}".format(temp_num, a_dir[slash_index:]))
            temp_num +=1

    def user_input(self):
        temp_response = input(">>>")
        if temp_response.lower() in ('q', 'quit'):
            exit()
        else:
            return temp_response

    def main(self):
        #maps out current working dir
        self.find_dirs_in_cwd(self._root_dir)

        main_run = True
        while main_run == True:
            self.menu()
            response = self.user_input()
            self.logic(response)

    def logic(self, a_user_input):
        if int(a_user_input) == 1:
            self.create_file()
        else:
            self._root_dir = self._dir_list[int(a_user_input)-1]
            print("Current Dir is {}".format(self._root_dir))
            self.find_dirs_in_cwd(self._root_dir)


    def create_file(self):
        print("What is the name of the file?")

        #tests if user placed .py in the string
        temp_name = self.user_input()
        print(temp_name)

        _class_setup1 = "class {}(): \n\n".format(temp_name)
        _class_setup2 = "    def __init__(self): \n"
        _class_setup3 = "        pass\n\n\n\n\n\n\n\n\n\n"
        _class_setup4 = "if __name__ == '__main__':\n"
        _class_setup5 = "    f = {}()".format(temp_name)

        temp_name = self.test_for_py(temp_name)

        if os.path.isfile(self._root_dir+"/"+temp_name):
            print("File Exists. Please enter a new name")
        else:
            file = open(os.path.join(self._root_dir,temp_name), 'w')

            #setting up the py file as preferred
            file.writelines(self.python_file_list)
            file.write(_class_setup1)
            file.write(_class_setup2)
            file.write(_class_setup3)
            file.write(_class_setup4)
            file.write(_class_setup5)


            file.close()
            print("File Created")
            exit()

    """Tests for .py extension. If non,
        it places it for them"""
    def test_for_py(self, a_string):
        if ".py" in a_string:
            return a_string
        else:
            return a_string+".py"

    """Tests to see if file is in support class file.
        If it is, it returns the dir above it"""
    def set_main_dir(self):
        temp_string = os.getcwd()
        if self.support_dir in temp_string:
            return temp_string.replace(self.support_dir, "")
        else:
            print("Uhoh")



if __name__ == '__main__':
    f = CreateStandardFile()
    f.main()