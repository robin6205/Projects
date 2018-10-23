from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import os
import time

TEST_DIRECTORY = 'test 1'
headless = True
user = 'chang529'
user_p = '#password'
term = 'Fall 2018'

def make_dir(directory):
    """
    #
    Creates the specified directory in the current directory.
    #
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('Directory created at ' + directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def element_exists(browser, xpath):
    """
    #
    Takes an xpath and browser and checks if the specified element exists in the browser.
    #
    """
    if len(browser.find_elements_by_xpath(xpath)) is 0:
        return(False)
    else:
        return(True)

chrome_options = Options()
if headless:
    chrome_options.add_argument("--headless")

browser = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', chrome_options=chrome_options)

# navigate to database
print('Navigating to database')
browser.get('https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu%2Fc%2Fportal%2Flogin')
print(browser.title)
user_elem = browser.find_element_by_name('username')
print('Login user: ' + user)
user_elem.send_keys(user)
pass_elem = browser.find_element_by_name('password')
print('Login pass: ' + (len(user_p) * '*'))
pass_elem.send_keys(user_p + Keys.RETURN)
print('Logging in...')
browser.get('https://wl.mypurdue.purdue.edu/web/portal/registration')
print('...Done')
print(browser.title)
reg_elem = browser.find_element_by_link_text('Look Up Classes')
reg_elem.click()
browser.switch_to_window(browser.window_handles[1])
print(browser.title)
term_elem = browser.find_element_by_xpath('//*[@id="term_input_id"]')
select = Select(term_elem)
select.select_by_visible_text(term)
print('Term: ' + term)
term_elem.send_keys(Keys.ENTER)
print(browser.title)


# Select a school
subj_list_elem = browser.find_element_by_xpath('//*[@id="subj_id"]')
subj_select = Select(subj_list_elem)

acronym_array = []
for subject in subj_select.options:
    acronym = subject.get_attribute('value')
    subj_select.select_by_value(acronym)
    make_dir(TEST_DIRECTORY + '/' + acronym)
    acronym_array.append(acronym)

print('Loading classes...')
subj_list_elem.send_keys(Keys.ENTER)
print('...Done')


# Step through each subject
for i in range(len(acronym_array)):
    subj_xpath = '/html/body/div[3]/table[' + str(2 + i) + ']'
    acronym = acronym_array[i]

    table = browser.find_elements_by_xpath(subj_xpath + '/tbody/tr')
    for j in range(2, len(table) - 1):
        class_name = table[j].text
        make_dir(TEST_DIRECTORY + '/' + acronym + '/' + class_name)
