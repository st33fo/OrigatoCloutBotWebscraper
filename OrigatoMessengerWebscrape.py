# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:10:03 2019

@author: Stefan
"""

from selenium import webdriver

from flask import Flask, render_template, session

app = Flask(__name__)
#I should comment my code


'''
Web driver will open up the chrome page and simulate whatever function
your bot does. Feed it the URL and it goes to the page.
'''
driver = webdriver.Chrome()

driver.get("https://www.messenger.com/t/1738204539622881")

#Verifies this is the messenger facebook page. Not really necessary,

assert "Messenger" in driver.title
'''
Finds web elements of the username and password inputs on the page.
Should only be used initially by the bot. 
I originally had this inside of the flask webpage but it got annoying
cause it kept opening chrome every time i refreshed the page. So now it will just
login once and open chrome once. The rest will just be in page refreshes.
'''
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

userinput = 'Your user name'
userpass = 'Your password'
username.send_keys(userinput)
password.send_keys(userpass)
   
#simulates the press of the logni button.
driver.find_element_by_name("login").click()


@app.route('/messages') 
def messages():
    '''
    The next lines of code target the specific tag that holds the information
    we're looking for. The driver is pretty much the entire messenger webpage,
    then page hones in on just the messenger box. Subpage goes down to just the 
    chat in the messenger's box. We keep zoning in until we hit to our messages
    which I've stored in messages. The 'messages' variable now holds a list of the
    messages.
    '''

    page = driver.find_element_by_class_name("_2sdm")
    subpage = page.find_element_by_class_name("_4_j4")
  
    subpage2 = subpage.find_element_by_css_selector('._4u-c._1wfr._9hq')

    
    messages = subpage2.find_elements_by_css_selector('._1t_p.clearfix')
    
    #returns an html page which has already been defined and prewritten
    return render_template('Messages.html', messages = messages)

#makes it so that when I save, the server automatically reloads.
if __name__ == "__main__":
    app.run(debug=True)