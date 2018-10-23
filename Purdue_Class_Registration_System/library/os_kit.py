"""
File: os_kit.py


A collection of code snippets that are useful for operating-system functions.
Not intended to be static, functions and classes will be added on an as-needed
basis.
"""


#------------------------------------------------------------------------------


"""
Imports
"""
import os


#------------------------------------------------------------------------------


def get_cwd():
    """
    Runs the os.getcwd() command. Returns the current working directory string.
    Included for consistent structure.
    """
    return(os.getcwd())


#------------------------------------------------------------------------------


def log_error(error):
    """
    Logs errors in the log file. currently unimplemented, just prints the error
    """
    print(error)


#------------------------------------------------------------------------------


def make_dir(directory):
    """
    Creates the specified directory within the current working directory. If
    the directory already exists, no action is performed.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('Directory created at ' + directory)
    except OSError as error:
        print ('Error: Creating directory. ' +  directory)
        log_error(error)


#------------------------------------------------------------------------------


def get_dir(directory):
    """
    Gets the full directory pathname for a specified directory inside the
    master direc.: i.e. if you ask for 'users' you get 'purdue classes scraper/
    users'. Returns the master directory if an invalid directory is returned.
    Creates the directory if it does not exist.
    """
    try:
        new_directory = get_cwd()[:-7] + directory
    except TypeError:
        return(get_cwd()[:-7])

    make_dir(new_directory)
    return(new_directory)


#------------------------------------------------------------------------------
