from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import getcwd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import time



chrome_options = Options()
#chrome_options.add_argument("--headless")


browser = webdriver.Chrome(executable_path=getcwd() + '/chromedriver', chrome_options=chrome_options)
main_window = browser.current_window_handle

browser.get('https://www.purdue.edu/apps/account/cas/login?service=https%3A%2F%2Fwl.mypurdue.purdue.edu%2Fc%2Fportal%2Flogin')
assert 'Purdue' in browser.title

user_elem = browser.find_element_by_name('username')
user_elem.send_keys('chang529')
pass_elem = browser.find_element_by_name('password')
pass_elem.send_keys('#password' + Keys.RETURN)

browser.get('https://wl.mypurdue.purdue.edu/web/portal/registration')



reg_elem = browser.find_element_by_link_text('Look Up Classes')
reg_elem.click()

browser.switch_to_window(browser.window_handles[1])

term_elem = browser.find_element_by_xpath('//*[@id="term_input_id"]')
select = Select(term_elem)
select.select_by_visible_text('Fall 2018')
term_elem.send_keys(Keys.ENTER)

schl_elem = browser.find_element_by_xpath('//*[@id="subj_id"]')
select = Select(schl_elem)
select.select_by_value('AAE')
schl_elem.send_keys(Keys.ENTER)
'''
while len(browser.find_elements_by_xpath('/html/body/div[3]/table[2]/tbody/tr[3]/td[3]/form/input[30]')) is 0:
    time.sleep(0.05)

bttn_elem = browser.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[3]/td[3]/form/input[30]')
bttn_elem.click()

browser.save_screenshot('headless test.png')

browser.
'''

browser.execute_script('submitcount = 0')
