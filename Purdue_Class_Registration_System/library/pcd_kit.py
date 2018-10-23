"""
File: pcd_kit.py

Toolkit for interfacing with the Purdue classes database, for easy database
access. Runs using Selenium and Chromium. A webdriver object MUST be passed here
for the interfacing code to run properly.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from os_kit import *
from purdue_user import User

import time

global browser  # webdriver
global user     # User


"""
Defaults and URLs
"""
LOGIN_PAGE = 'https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu'
REGISTRATION_PAGE = 'https://wl.mypurdue.purdue.edu/web/portal/registration'





def set_webdriver(arg_browser):
    """
    Sets the global webdriver object 'browser'. The pcd_kit is given control
    over the specified driver.
    """
    global browser
    browser = arg_browser





def set_user(arg_user):
    """
    Sets the global User object 'user'. The pcd_kit uses this user to login to
    mypurdue.
    """
    global user
    user = arg_user





def goto_tab(number):
    """
    Sets browser control to tab 'number', numbered starting from 0 from left to
    right.
    """
    browser.switch_to_window(browser.window_handles[number])





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
    browser.close() # close the now useless registration tab
    goto_tab(0)

    # Enter the desired term
    term_elem = browser.find_element_by_xpath('//*[@id="term_input_id"]')
    select = Select(term_elem)
    select.select_by_visible_text(term_use)
    term_elem.send_keys(Keys.ENTER)





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





def select_subject(*args):
    """
    Enters the desired subject(s) into the subject selection screen. Any
    number of subjects can be passed as args; if none are passed then all are
    selected. Does not do anything if the browser is not at this screen.
    Returns the number of subjets opened (this could be useful in the future)
    """
    # Set up a Select object
    subj_list_elem = browser.find_element_by_xpath('//*[@id="subj_id"]')
    subj_select = Select(subj_list_elem)

    # Select all passed subjects
    if len(args) is 0:
        for subject in subj_select.options:
            subj_select.select_by_values(subject.get_attribute('value'))
        count = len(subj_select.options)
    else:
        for arg in args:
            subj_select.select_by_value(arg)
        count = len(args)

    subj_list_elem.send_keys(Keys.COMMAND + Keys.ENTER)
    return(count)







temp = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver')
set_webdriver(temp)
set_user(User(file='mc.json'))
goto_database()
