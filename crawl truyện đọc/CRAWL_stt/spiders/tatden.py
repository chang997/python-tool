# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:21:05 2019

@author: Admin
"""
import scrapy
from selenium import webdriver


class tatden(scrapy.Spider):
    name= "tatden"
    start_urls = ['https://www.sachhayonline.com/tua-sach/tat-den']
    
    def parse(self, response):
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
        driver.get(response.url)
        
        chapters = driver.find_elements_by_xpath('//*[@id="content"]/ul/li/a')
        urls=[]
        titles=[]
        for chapter in chapters:
            urls.append(chapter.get_attribute("href"))
            titles.append(chapter.text)
        
        for (url,title) in zip(urls, titles):
            driver.get(url)
            text = driver.find_elements_by_xpath('//*[@id="content"]/article/p')
            for t in text:
                with open('Data/NgoHong/tat_den/'+title+'.txt', "a", encoding="utf-8") as f:
                    f.write('\n'+t.text)
                    
                
                
                
            
            
            
        
