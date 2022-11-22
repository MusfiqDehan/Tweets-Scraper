# Import Libraries

import re
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Library for different Browsers

# Firefox
from selenium.webdriver import Firefox

# Google Chrome
# from selenium.webdriver import Chrome

# Microsoft Edge
# from msedge.selenium_tools import Edge, EdgeOptions

# Driver for different Browsers

# Firefox
driver = Firefox()

# Google Chrome
# driver = Chrome()

# Microsoft Edge
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options=options)

driver.get(url="https://twitter.com/i/flow/login")

your_name = str(input("Enter your username: "))
your_pass = getpass("Enter your password")

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys(your_name)
username.send_keys(Keys.RETURN)
sleep(3)

ok_btn = driver.find_element(By.XPATH, "//span[contains(text(),'OK')]")
sleep(5)
ok_btn.click()

# If recapcha appears we have to manually solve it
# Manually Solve Recaptcha

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys(your_pass)
password.send_keys(Keys.RETURN)
sleep(3)
