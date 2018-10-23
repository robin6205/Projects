"""
File: master_update.py


Updates the entire database. Note from creator: I opted to not utilize the
ability of the pull_info_from_subject_screen() function to pull ALL courses
with one function call, because it seemed smarter to pull little 'chunks' of
data and save periodically as we go... these 'chunks' are, for sake of
simplicity, subjects.
"""


#------------------------------------------------------------------------------


"""
Imports
"""
import lcd_kit as lcd
import pcd_kit as pcd
from os_kit import get_dir
from purdue_user import User

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#------------------------------------------------------------------------------


TERM = 'Fall 2018'


# Set up webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=get_dir('chromedriver'),\
                           chrome_options=chrome_options)
pcd.set_webdriver(browser)

# Set up User
user = User(file='mc.json')
pcd.set_user(user)

# Navigate to subject screen
print('##### MASTER UPDATE #####')
print('Navigating to through mypurdue...')
pcd.goto_database()
print('Entering term:', TERM)
pcd.select_term(TERM)
print('Selecting all subjects...')
pcd.select_subject(update=True)
pcd.wait_for_screen('subject')

# Get tables dictionary
print('Getting tables dictionary...')
tables_dict = pcd.get_tables_dict_from_subject_screen()

num_subjects_left = len(pcd.all_subjects)
for subject in pcd.all_subjects:
    # messy but working way of getting number of courses
    temp_elem = tables_dict[subject].find_elements_by_xpath('*')[0]
    num_courses = len(temp_elem.find_elements_by_xpath('*')) - 2

    print('\n----------------------------')
    print('BEGIN PULLING SUBJECT:', subject)
    print('Number of courses:', num_courses)
    print('Subjects remaining:', num_subjects_left)
    print('----------------------------')

    # Gets the data
    pulled_dictionary = pcd.pull_info_from_subject_screen(subject=subject,\
                                                       tables_dict=tables_dict)

    # Saves the data
    print('\nSubject pulled. Saving subject...')
    lcd.save_info(pulled_dictionary, subject=subject)

    num_subjects_left -= 1
