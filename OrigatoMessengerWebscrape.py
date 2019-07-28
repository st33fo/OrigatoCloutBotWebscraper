# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:10:03 2019

@author: Stefan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask,request, render_template
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
app = Flask(__name__)
#I should comment my code

@app.route('/')
def login():
    
    driver = webdriver.Chrome()
    
    driver.get("https://www.messenger.com/t/1738204539622881")
    
    assert "Messenger" in driver.title
    
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    
   # userinput = input("Username Please")
   # userpass = input("Password Please")
    
    userinput = 'Your user name'
    userpass = 'Your password'
    username.send_keys(userinput)
    password.send_keys(userpass)
    messageslist =[]
    driver.find_element_by_name("login").click()
    
    page = driver.find_element_by_class_name("_2sdm")
    subpage = page.find_element_by_class_name("_4_j4")
   #subpage2 = subpage.find_elements_by_xpath('//div')
    wait = WebDriverWait(subpage,10)
    subpage2 = subpage.find_element_by_css_selector('._4u-c._1wfr._9hq')

    
    messages = subpage2.find_elements_by_css_selector('._1t_p.clearfix')
    
    
    return render_template('Messages.html', messages = messages)


if __name__ == "__main__":
    app.run(debug=True)