# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:16:32 2019

@author: Admin

auto search on chrome with selenium 
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
browser.get('https://translate.google.com/?hl=vi#view=home&op=translate&sl=vi&tl=en')

search = browser.find_element_by_xpath('//*[@id="source"]')
search.send_keys(text)
#search.send_keys(Keys.RETURN) # tab to down the line
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[5]/div[3]/div[2]').click() 
                                # click to hear voice
# get response url by click button ????????????????????????????????????????
browser.quit() # off browser 