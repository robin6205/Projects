"""
File: purdue_user.py

Contains the class definition for a User object, a simple class with
attributes for a valid Purdue login. This could be a little better executed,
but it works and it doesn't have to much.
"""


#------------------------------------------------------------------------------


"""
Imports
"""
from os_kit import get_cwd, get_dir


#------------------------------------------------------------------------------


class User:
    """
    A class for a Purdue user. Used to log in to mypurdue with valid username
    and password attributes
    """
    def __init__(self, *args, **kwargs):
        """
        username and password can be passed through kwargs, or a pathname to a
        file containing the username and password can be passed.
        """
        if 'file' in kwargs:
            self.input_path = get_dir('users') + '/' + kwargs['file']
            f = open(self.input_path, 'r')
            input_lines = f.read().splitlines()
            f.close()

            self.username = input_lines[0]
            self.password = input_lines[1]

        else:
            if 'username' in kwargs:
                self.username = kwargs['username']
            else:
                self.username = ''

            if 'password' in kwargs:
                self.password = kwargs['password']
            else:
                self.password = ''


    #--------------------------------------------------------------------------


    def save(self, *args, **kwargs):
        """
        Saves the user data. If a pathname is passed as an argument, data is
        saved to the given pathname. Otherwise, the data is saved to the input
        path (if it exists).
        """
        try:
            save_path = self.input_path
        except AttributeError:
            pass

        for arg in args:
            if type(arg) is str:
                save_path = get_cwd()[:-7] + 'users/' + arg

        try:
            with open(save_path, 'w+') as f:
                f.write(self.username + '\n' + self.password)
                f.close()
        except NameError:
            print('Error saving user data: no file path provided')
