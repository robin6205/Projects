"""
File: pcd_kit.py


Toolkit for interfacing with the Purdue classes database, for easy database
access. Runs using Selenium and Chromium. A webdriver and a user object MUST be
passed here for the interfacing code to run properly.
"""


#------------------------------------------------------------------------------


"""
Imports
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from os_kit import get_dir
import os
import json
from purdue_user import User

import time


#-----------------------------------------------------------------------------


"""
Global variables
"""
global browser  # webdriver
global user     # User
global all_subjects # list of all subjects offered by Purdue

# Load the subjects list
filename = get_dir('data') + '/subjects.json'
with open(filename, 'r', encoding="utf8") as infile:
    all_subjects = json.load(infile)


#------------------------------------------------------------------------------


"""
Defaults and URLs
"""
LOGIN_PAGE = 'https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu'
REGISTRATION_PAGE = 'https://wl.mypurdue.purdue.edu/web/portal/registration'


#------------------------------------------------------------------------------


def set_webdriver(arg_browser):
    """
    Sets the global webdriver object 'browser'. The pcd_kit is given control
    over the specified driver.
    """
    global browser
    browser = arg_browser


#------------------------------------------------------------------------------


def set_user(arg_user):
    """
    Sets the global User object 'user'. The pcd_kit uses this user to login to
    mypurdue.
    """
    global user
    user = arg_user


#------------------------------------------------------------------------------


def goto_tab(arg):
    """
    Sets browser control to tab 'number', numbered starting from 0 from left to
    right.
    """
    browser.switch_to_window(browser.window_handles[arg])


#------------------------------------------------------------------------------


def login():
    """
    Enters user's data into mypurdue and logs in.
    """
    # Ensure the browser is on the login page
    if 'Purdue Web Authentication' not in browser.title:
        browser.get(LOGIN_PAGE)

        # Case for if the browser is already logged in
        if 'Academics - purdue.edu' in browser.title:
            browser.get(REGISTRATION_PAGE)
            return

    # Get the username and password elements and enter login
    user_elem = browser.find_element_by_name('username')
    pass_elem = browser.find_element_by_name('password')
    user_elem.send_keys(user.username)
    pass_elem.send_keys(user.password + Keys.RETURN)


#------------------------------------------------------------------------------


def goto_database(*args, **kwargs):
    """
    Navigates the browser to the front of the database. Can take a 'term' arg,
    otherwise uses the default term.
    """
    browser.get(REGISTRATION_PAGE)

    if 'Purdue Web Authentication' in browser.title: # Login screen
        login()

    # At this point, we are at the registration page. Navigate to database
    reg_elem = browser.find_element_by_link_text('Look Up Classes')
    reg_elem.click()

    # if necessary, close the now useless registration tab
    if len(browser.window_handles) > 1:
        browser.close()
        goto_tab(0)


#------------------------------------------------------------------------------


def select_term(term_use):
    """
    Enters the desired term into the 'select term or data range' screen.
    Does not do anything if the browser is not at this screen.
    """
    if 'Select Term or Date Range' not in browser.title:
        print('Error selecting term: Not at the correct screen')
    else:
        # Enter the desired term
        term_elem = browser.find_element_by_xpath('//*[@id="term_input_id"]')
        select = Select(term_elem)
        select.select_by_visible_text(term_use)
        term_elem.send_keys(Keys.ENTER)


#------------------------------------------------------------------------------


def select_subject(*args, **kwargs):
    """
    Enters the desired subject(s) into the subject selection screen. Any
    number of subjects can be passed as args; if none are passed then all are
    selected. Assumes browser is at this screen.
    Returns the number of subjects opened (this could be useful in the future)

    If update=True is passed, the global list of all_subjects is updated.
    """
    # Set up a Select object
    subj_list_elem = browser.find_element_by_xpath('//*[@id="subj_id"]')
    subj_select = Select(subj_list_elem)
    subj_select.deselect_all()



    # Update the all_subjects list if required
    if 'update' in kwargs:
        if kwargs['update']:

            new_list = []
            for option in subj_select.options:
                new_list.append(option.text.split('-')[0])
            global all_subjects
            all_subjects = new_list

            filename = get_dir('data') + '/subjects.json'
            with open(filename, 'w', encoding="utf8") as outfile:
                json.dump(all_subjects, outfile, sort_keys=True, indent=4)

        print('Updated subjects.json')



    # Select all passed subjects
    if len(args) is 0:
        for subject in subj_select.options:
            subj_select.select_by_value(subject.get_attribute('value'))
        count = len(subj_select.options)
    else:
        for arg in args:
            subj_select.select_by_value(arg)
        count = len(args)

    # Enter the subjects
    subj_list_elem.send_keys(Keys.ENTER)
    return(count)


#------------------------------------------------------------------------------


def wait_for_screen(screen):
    """
    Waits until the specified screen, 'subject' or 'course' has loaded by
    simply waiting until a pre-determined element is loaded. The elements that
    are used are used because their existence guarantees that all useful elems
    are on screen.
    """
    if screen == 'subject':
        xpath = '/html/body/div[3]/table[2]/tbody/tr[3]/td[3]/form/input[30]'
    elif screen == 'course':
        xpath = '/html/body/div[3]/form/table/tbody/tr[3]/td[4]'

    elem = browser.find_elements_by_xpath(xpath)
    while len(elem) is 0:
        elem = browser.find_elements_by_xpath(xpath)
        time.sleep(0.05)


#------------------------------------------------------------------------------


def get_tables_dict_from_subject_screen():
    """
    Gets the tables dictionary from the subject screen... obviously
    This dictionary is keyworded by subject and contains the table element for
    each subject.
    """
    # Get all the HTML tables containing the rows for each
    # course. Remove the first 3 and last 2 elements as they are not courses.
    body = browser.find_element_by_xpath('/html/body/div[3]') # tables' parent
    tables_array = body.find_elements_by_xpath('*')[3:][:-2]

    # For each table, sort the course elements into a dictionary keyworded by
    # the subject they fall under
    tables_dict = {}
    for table in tables_array:
        subject = table.find_element_by_xpath('tbody/tr[2]').text.split('-')[0]
        tables_dict[subject] = table

    return(tables_dict)


#------------------------------------------------------------------------------


def pull_info_from_subject_screen(**kwargs):
    """
    Navigates from the subject screen to a course screen, then pulls the course
    information using pull_info_from_course_screen().
    Courses can be specified in *args, for example:
    course='AAE 20000' OR subject='AAE', number='20000'
    Subjects can also be specified in *args, for example: subject='AAE'
    If neither are specified, then all courses on screen are pulled.

    A keyworded tables dictionary can also be passed to speed up computations:
    tables_dict = tables_dict
    This dictionary is keyworded by subject and contains table elements.

    If nothing is specified return is standard ['Subj']['Crse']['Sect']['Flag']
    If a subject is specified return is ['Crse']['Sect']['Flag']
    If a course is specified return is ['Sect']['Flag']
    """
    # This block gets the table dictionary. If one is passed through kwargs,
    # then (obviously) this block can be skipped.
    if 'tables_dict' in kwargs:
        tables_dict = kwargs['tables_dict']

    else:
        tables_dict = get_tables_dict_from_subject_screen()

    # Now figure out what course(s) we want.
    want_subj = False
    want_numb = False
    if 'subject' in kwargs:
        want_subj = kwargs['subject']
        if 'number' in kwargs:
            want_numb = kwargs['number']
    elif 'course' in kwargs:
        want_subj = kwargs['course'].split(' ')[0]
        want_numb =  kwargs['course'].split(' ')[1]



    # This block is executed if we want a specific course.
    if want_subj and want_numb:

        # Get the subject's table element.
        try:
            table = tables_dict[want_subj]
        except KeyError:
            print('Error getting course info [', want_subj, want_numb, ']: tables_dict error')
            return

        # Get the button element for the course.
        locator_xpath = "//*[@name='SEL_CRSE'][@value='" + want_numb + "']"
        locator_elem = table.find_element_by_xpath(locator_xpath)
        button_elem = locator_elem.find_element_by_xpath("following-sibling::*[@name='SUB_BTN']")

        # Open the course info in a new tab. Wait until page is loaded, then
        # pull the course info. Then close the ab.
        button_elem.send_keys(Keys.COMMAND + Keys.RETURN)
        goto_tab(1)
        wait_for_screen('course')
        return_dict = pull_info_from_course_screen()
        browser.close()
        goto_tab(0)
        browser.execute_script('submitcount = 0') # thanks, purdue.



    # This block is executed if we want all courses in a specific subject.
    elif want_subj:
        return_dict = {}

        # Get the subject's table element.
        try:
            table = tables_dict[want_subj]
        except KeyError:
            print('Error getting course info [', want_subj, '##### ]: tables_dict error')
            return

        # Get all the locator elements for the subject.
        locator_elems = table.find_elements_by_name('SEL_CRSE')

        # For each locator, get the button element then get info (like above)
        for locator_elem in locator_elems:
            button_elem = locator_elem.find_element_by_xpath("following-sibling::*[@name='SUB_BTN']")
            course_number = locator_elem.get_attribute('value')

            button_elem.send_keys(Keys.COMMAND + Keys.RETURN)
            goto_tab(1)
            wait_for_screen('course')
            return_dict[course_number] = pull_info_from_course_screen()
            browser.close()
            goto_tab(0)
            browser.execute_script('submitcount = 0') # thanks, purdue.



    # This block is executed if we want all courses.
    else:
        return_dict = {}

        # Get all the subjects from the tables_dict. Then use recursion to get
        # the info for each subject.
        subjects = list(tables_dict.keys())
        for subject in subjects:
            return_dict[subject] = pull_info_from_subject_screen(\
                                   tables_dict=tables_dict,\
                                   subject=subject)



    return(return_dict)


#------------------------------------------------------------------------------


def pull_info_from_course_screen():
    """
    Pulls all the information off of a course page. Assumes browser is at a
    course page. Returns a dictionary with the following info:
    returned_dictionary['Course Section Number]
    'CRN': course registration number
    'SBJ': subject
    'CRS': course number
    'SEC': section number
    'CMP': campus (usually PWL)
    'CRD': credits
    'TTL': title
    'DAY': meeting days
    'TME': meeting time
    'CAP': number of seats
    'ACT': number of filled seats
    'REM': number of remaining seats
    'INS': instructor
    'DTE': date
    'LOC': location
    'TYP': type (lecture, lab, etc)
    'LKS': links (???)
    'REQ': requisites (to be finished later)
    'NTS': notes
    'ATR': attributes (lower division, etc)
    """
    # Get all row elements
    table = browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody')\
            .find_elements_by_xpath('*')[2:]

    # FOR EACH COURSE SECTION
    return_dict = {}
    for section in table:
        sn = section.find_element_by_xpath('td[5]').text
        subj = section.find_element_by_xpath('td[3]').text
        numb = section.find_element_by_xpath('td[4]').text
        return_dict[sn] = {}
        return_dict[sn]['CRN'] = section.find_element_by_xpath('td[2]').text
        return_dict[sn]['SBJ'] = subj
        return_dict[sn]['CRS'] = numb
        return_dict[sn]['SEC'] = sn
        return_dict[sn]['CMP'] = section.find_element_by_xpath('td[6]').text
        return_dict[sn]['CRD'] = section.find_element_by_xpath('td[7]').text
        return_dict[sn]['TTL'] = section.find_element_by_xpath('td[8]').text
        return_dict[sn]['DAY'] = section.find_element_by_xpath('td[9]').text
        return_dict[sn]['TME'] = section.find_element_by_xpath('td[10]').text
        return_dict[sn]['CAP'] = section.find_element_by_xpath('td[11]').text
        return_dict[sn]['ACT'] = section.find_element_by_xpath('td[12]').text
        return_dict[sn]['REM'] = section.find_element_by_xpath('td[13]').text
        return_dict[sn]['INS'] = section.find_element_by_xpath('td[20]').text
        return_dict[sn]['DTE'] = section.find_element_by_xpath('td[21]').text
        return_dict[sn]['LOC'] = section.find_element_by_xpath('td[22]').text
        return_dict[sn]['TYP'] = section.find_element_by_xpath('td[23]').text
        return_dict[sn]['LKS'] = section.find_element_by_xpath('td[24]').text
        return_dict[sn]['REQ'] = section.find_element_by_xpath('td[25]').text
        return_dict[sn]['NTS'] = section.find_element_by_xpath('td[26]').text
        return_dict[sn]['ATR'] = section.find_element_by_xpath('td[27]').text


    print('Pulled course:', subj, numb)
    return(return_dict)


#------------------------------------------------------------------------------
