# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""


import scrapy
import time
from selenium import webdriver
import pandas as pd



class ThegioididongSpider(scrapy.Spider):
    name = 'thegioididong'
    allowed_domains = ['thegioididong.com']
    start_urls = ['https://www.thegioididong.com/dtdd/iphone-xr?fbclid=IwAR37j7COpuL6pj44dhHTRkzctAJNdniJlmZUgpmjw-AaL1131yHk1Uv8l6g']

    def parse(self, response):
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
        driver.get(response.url)
        
        chat = []
        chat = chat + self.detail(driver)
        
        i=1
        while True:
            try:
                button = driver.find_elements_by_xpath('//div[@class="wrap_comment"]/ul[@class="listcomment"]/div[@class="pagcomment"]/span[@class="active"]/following-sibling::a[1]')
                button[0].click()
            except:
                break 
            
            print (i)
            i = i+1
            
            data = self.detail(driver)
            if len(data)!=0:
                chat = chat + data
        
        driver.close()
        
        df = pd.DataFrame(chat)
        df.to_csv(r'DATA/thegioididong.csv')
        
        print('--------------------------------JOB DONE--------------------------------')


    def detail(self, driver):
        time.sleep(19)
        
        chat = []
        elements = driver.find_elements_by_xpath('//ul[@class="listcomment"]/li')
        for e in elements:
            try: 
                question = e.find_element_by_xpath('div[@class="question"]').text
                answer = e.find_element_by_xpath('div[@class="listreply"]/div[@class="reply "][1]/div[@class="cont"]').text.replace("\n", " ")
                chat.append([question, answer])
            except:
                continue
            
        return (chat)