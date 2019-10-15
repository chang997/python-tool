# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:34:49 2019

@author: Admin
"""
import scrapy
from selenium import webdriver
import urllib
import os

class NgoHong(scrapy.Spider):
    name = 'NgoHong'
    start_urls = ['http://sachnoiviet.com/sach-noi/700/tat-den.html',
                  'http://sachnoiviet.com/sach-noi/1024/nhung-ngay-tho-au.html']

    def parse(self, response):
        name = response.url.split('/')[-1].split('.')[0].replace('-','_')
        os.mkdir('Data/NgoHong/'+name)
        
        driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
        driver.get(response.url)

        xpaths = driver.find_elements_by_xpath('//*[@id="jp_container_1"]/div/div[2]/ul/li/div/span/a')
        urls=[]
        for xpath in xpaths:
            urls.append(xpath.get_attribute("href"))
            
        for url in urls:
            chapter=url.split('/')[-1].split('.')[0]
            urllib.request.urlretrieve(url, 'Data/NgoHong/'+name+'/'+chapter+'.mp3')
# =============================================================================
#             mp3file = urllib.request.urlopen(url)
#             chapter=url.split('/')[-1].split('.')[0]
#             
#             output = open('Data/NgoHong/'+name+'/'+chapter+'.mp3','wb')
#             output.write(mp3file.read())
#             output.close()
#             
#             
# =============================================================================
            
            
            
        
