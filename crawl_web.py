
import time
from selenium import webdriver
import pandas as pd



class Admicro():

    def get_all(web_url):
        driver = webdriver.Chrome(r"//path to driver")
        driver.get(web_url)

        name_categorys = driver.find_elements_by_xpath('//ul[@class='main-menu']/li').text   # tên tương ứng của từng chủ đề
        self.links = {}        # các đường dẫn của từng bài viết
        self.info = []      # thông tin cần lấy     

        for i in range(1, len(name_categorys)):    
            if i==1:
                continue
            else:
                name_category = name_categorys[i]
                url_subcategorys = driver.find_elements_by_xpath('//ul[@class='sub-menu']'+str([i-1])+'/li/a').get_attribute("href")  # tất cả các chủ đề con
                for url in url_subcategorys:
                    self.links[name_category] = self.get_link(url)       # lấy tất cả link bài viết trong từng chủ đề
            
        for name_category in self.links:
            links = self.links[name_category]
            for link in links:
                self.info += self.info(self, name_category, link)   #lấy thông tin trong từng bài viết
    
        df = pd.DataFrame(info)
        df.to_csv(r'info.csv')
        
        print('--------------------------------JOB DONE--------------------------------')

    def get_link(self, url_category):   # lấy link bài viết trong từng chủ đề
        self.driver.get(url_category)
        links = self.driver.find_elements_by_xpath('//ul[@class='other_post']/li/a').get_attribute("href") 

        while True :
            try:
                next_page = self.driver.find_elements_by_xpath('//ul[@class='paging-item'][7]').get_attribute("href") 
                self.driver.get(next_page) 
                time.sleep(5)

                links.append(self.driver.find_elements_by_xpath('//ul[@class='other_post']/li/a').get_attribute("href")) 
            except:
                next_page = self.driver.find_elements_by_xpath('//ul[@class='paging-item'][6]').get_attribute("href") 
                self.driver.get(next_page) 
                time.sleep(5)

                links.append(self.driver.find_elements_by_xpath('//ul[@class='other_post']/li/a').get_attribute("href")) 
                break

        return(links)


    def details(self, name_category, link):
        self.driver.get(link)
        time.sleep(10)
        
        name_content = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/h1').text
        author = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/p/b').text
        date = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/p/text()')

        return ([name_category, name_content, link, author, date])         
