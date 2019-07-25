# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:10:03 2019

@author: Stefan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask,request, render_template
import time
app = Flask(__name__)
#I should comment my code

@app.route('/')
def login():
    
    driver = webdriver.Chrome()
    
    driver.get("https://www.messenger.com/t/1738204539622881")
    
    assert "Messenger" in driver.title
    
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    
#    userinput = input("Username Please")
#    userpass = input("Password Please")
    
    userinput = 'your user name'
    userpass = 'and password'
    username.send_keys(userinput)
    password.send_keys(userpass)
    messages =[]
    driver.find_element_by_name("login").click()
    
    page = driver.find_element_by_class_name("_2sdm")
    subpage = page.find_element_by_class_name("_4_j4")
    subpage2 = subpage.find_elements_by_xpath('//div')
   
    allelements = len(subpage2)
    for subs in range(allelements):
        messages.append(subpage2[subs])
    
    return render_template('Messages.html', messages = messages)


if __name__ == "__main__":
    app.run(debug=True)