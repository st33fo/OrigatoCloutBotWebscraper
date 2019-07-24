# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:10:03 2019

@author: Stefan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.messenger.com/t/1738204539622881")

assert "Messenger" in driver.title

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

userinput = input("Username Please")
userpass = input("Password Please")
username.send_keys(userinput)
password.send_keys(userpass)

driver.find_element_by_name("login").click()

page = driver.find_element_by_class_name("_2sdm")

print(page)

