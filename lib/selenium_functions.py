#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from dotenv import load_dotenv
import os

# load real debrid login credentials
load_dotenv()
username = os.getenv('RD_USER')
password = os.getenv('RD_PASS')

# set chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('log-level=3')
options.add_argument('--disable-gpu')
options.add_argument('--disable-notifications')
# initiate webdriver
service = Service(r'/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# URLS to use
real_debrid = 'https://real-debrid.com'
url_1337x = 'https://1337x.to/search/'
i2psnark = 'http://127.0.0.1:7657/i2psnark/'

# function to scrape magnet link from https://1337x.to
def x1337x():
    # enter search query for torrent
    query = input("What do you want to download? ")
    query = query.replace(' ', '+')
    driver.get(f'{url_1337x}{query}/1/')
    # get list of torrents
    result_xpath = '//tr/td/a'
    results = WDW(driver, 12).until(EC.presence_of_all_elements_located((By.XPATH, result_xpath)))
    results = results[1:]
    new_results = []
    count = 0
    for index, result in enumerate(results):
        if index == 0:
            new_results.append(result)
            print(f'({str(count)}) {result.text}')
            count += 1
            continue
        if index % 3 != 0:
            continue
        else:
            new_results.append(result)
            print(f'({str(count)}) {result.text}')
            count += 1
    print('\n')
    # let user pick torrent
    torrent_selection = input('Select the number of the torrent you want: ')
    # get magnet link for selected torrent
    new_results[int(torrent_selection)].click()
    magnet_xpath = '//div/div/ul/li/a[@onclick="javascript: count(this);"]'
    magnet_elem = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, magnet_xpath)))
    magnet_link = magnet_elem.get_attribute('href')
    with open('.magnet_link', 'w') as f:
        f.write(magnet_link)



def rd_login():
	#  log in to real debrid
	driver.get(real_debrid)
	login_xpath = '//a[@id="allpage-login-top"]'
	login_button = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, login_xpath)))
	login_button.click()
	username_xpath = '//input[@name="username"]'
	password_xpath = '//input[@name="password"]'
	second_login_xpath = '//input[@id="submit"]'
	username_field = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, username_xpath)))
	username_field.send_keys(username)
	password_field = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
	password_field.send_keys(password)
	second_login_button = WDW(driver,  12).until(EC.presence_of_element_located((By.XPATH,  second_login_xpath)))
	second_login_button.click()
	time.sleep(2)
	driver.get(f'{real_debrid}/torrents')
	time.sleep(2)
	cookie_prompt_xpath = '//a[@id="cookieChoiceDismiss"]'
	cookie_prompt = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, cookie_prompt_xpath)))
	if cookie_prompt:
		cookie_prompt.click()



def start_torrent():
	# start torrent
	start_torrent_xpath = '//input[@id="submit_files"]'
	start_button = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, start_torrent_xpath)))
	driver.execute_script('arguments[0].scrollIntoView(true);', start_button)
	start_button.click()


def start_i2p_torrent():
	# press start button in i2psnark
	driver.get(i2psnark)
	i2p_start_button_xpath = '//input[@title="Start the torrent"]'
	i2p_start_button = WDW(driver, 12).until(EC.presence_of_element_located((By.XPATH, i2p_start_button_xpath)))
	i2p_start_button.click()


def kill_chrome():
    driver.close()
    driver.quit()
