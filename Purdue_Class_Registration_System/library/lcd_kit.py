"""
File: ldc_kit.py

Toolkit for interfacing with the local classes database. Use this to pull data
from the local database.
"""


#------------------------------------------------------------------------------


"""
Imports
"""
from os_kit import get_dir
import json
import os


#------------------------------------------------------------------------------


def load_info(**kwargs):
    """
    Loads course info from the data directory.
    Returned dictionary follows standard formats:
    ['Number']['Section']['Flag'] for a subject
    OR
    ['Section']['Flag'] for a single course

    Can pass:
    subject = 'AAE'
    subject = 'AAE', number = '20000'
    course =  'AAE 20000'

    Loading all courses at once is NOT implemented for memory conservation
    reasons - load, at most, one subject at a time!
    """



    # This block runs if only one course is requested
    if ('number' in kwargs and 'subject' in kwargs) or ('course' in kwargs):
        if 'number' in kwargs and 'subject' in kwargs:
            subject = kwargs['subject']
            number = kwargs['number']
        elif 'course' in kwargs:
            subject = kwargs['course'].split()[0]
            number = kwargs['course'].split()[1]

        filename = get_dir('data/' + subject + '/' + subject + ' ' + number + '.json')
        with open(filename, 'r', encoding="utf8") as infile:
                return(json.load(infile))



    # This block runs if a full subject is requested
    elif 'subject' in kwargs:
        subject = kwargs['subject']
        directory = get_dir('data/' + subject)
        course_filenames = os.listdir(directory)

        return_dict = {}
        for course_filename in course_filenames:
            number = course_filename.split(' ')[1].split('.')[0]

            filename = directory + '/' + course_filename
            with open(filename, 'r', encoding="utf8") as infile:
                return_dict[number] = json.load(infile)

        return(return_dict)


    else:
        print('Error in load_course_info(): improper arguments')
        return


#------------------------------------------------------------------------------


def save_info(arg_dict, **kwargs):
    """
    Takes a standard dictionary (['Subject']['Number']['Section']['Flag']) and
    saves it to the data directory. Can also pass subject as a kwarg:
    ['Number']['Section']['Flag'], with subject as kwarg

    Format is data/[subject]/[subject + number].json
    """
    # simple addon to allow single-subject dictionaries to be passed
    if 'subject' in kwargs:
        course_dict = {kwargs['subject']:arg_dict}
    else:
        course_dict = arg_dict

    subj_keys = list(course_dict.keys())
    for subj in subj_keys:
        directory = get_dir('data/' + subj + '/')
        numb_keys = list(course_dict[subj].keys())

        for numb in numb_keys:
            filename = directory + subj + ' ' + numb + '.json'
            with open(filename, 'w', encoding="utf8") as outfile:
                json.dump(course_dict[subj][numb], outfile, sort_keys=True, indent=4)

            print('Saved course:', subj, numb)
