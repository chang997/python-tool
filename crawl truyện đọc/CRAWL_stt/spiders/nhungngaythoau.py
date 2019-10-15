# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:24:51 2019

@author: Admin
"""

import scrapy
from selenium import webdriver


class nhungngaythoau(scrapy.Spider):
    name= "nhungngaythoau"
    start_urls = ['https://sachvui.com/ebook/nhung-ngay-tho-au-nguyen-hong.2986.html']
    
    def parse(self, response):
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
        driver.get(response.url)
        
        chapters = driver.find_elements_by_xpath('//*[@id="list-chapter"]/li/a')
        urls=[]
        titles=[]
        for chapter in chapters:
            urls.append(chapter.get_attribute("href"))
            titles.append(chapter.text.split(":")[0].replace(" ",""))
        
        for (url,title) in zip(urls, titles):
            driver.get(url)
            text = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/p')
            for t in text:
                try:
                    with open('Data/NgoHong/nhung_ngay_tho_au/'+title+'.txt', "a", encoding="utf-8") as f:
                        f.write('\n'+t.text)
                except:
                    pass
                    
  