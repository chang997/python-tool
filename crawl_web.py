
import time
from selenium import webdriver
import pandas as pd



class Admicro:

	def __init__(self):
		self.driver = webdriver.Chrome(r"C:/Users/Admin/Desktop/chromedriver.exe")
		self.driver.get("https://marketingai.admicro.vn")
		self.links = {}        # các đường dẫn của từng bài viết
		self.info = []      # thông tin cần lấy    

	def get_all(self):
		driver_extra = webdriver.Chrome(r"C:/Users/Admin/Desktop/chromedriver.exe")     # vì subcategorys, sub đều được định nghĩa trên self.driver nên phải đảm bào self.drver không thay đổi

		categorys = self.driver.find_elements_by_xpath('/html/body/header/div[2]/div/div[4]/ul/li')  # từng chủ đề

		for i in range(1, len(categorys)-1):    # vì mục đầu là trang chủ và mục cuối không có bài viết
			print('-----------------------------------'+str(i)+'/'+str(len(categorys)-1))

			name_category = str(i)     # số thứ tư chủ đề
			subcategorys = categorys[i].find_elements_by_xpath('.//ul/li/a')     # các chủ đề con của từng mục

			for sub in subcategorys:
				url = sub.get_attribute("href")   #
				self.links[name_category] = self.get_link(driver_extra, url)       # lấy link bài viết trong từng chủ đề
		    
		for name_category in self.links:
		    links = self.links[name_category]
		    for url in links:
		        self.info.append(self.details(driver_extra, name_category, url))   #lấy thông tin từng bài viết
		        print(self.info)
		        

		df = pd.DataFrame(self.info, columns =['name_category', 'name_content', 'url', 'author'])
		df.to_csv(r'C:/Users/Admin/Desktop/admicro.txt', encoding='utf-8', sep=',')

		print('--------------------------------JOB DONE--------------------------------')

	def get_link(self, driver, url):   # lấy link bài viết trong từng chủ đề
	    driver.get(url)
	    links = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[2]/ul/li/div/h4/a") + \
	            driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li/div/h4/a")
	    links = [el.get_attribute("href") for el in links]

	    i = 1
	    while True :  
	    	try:
	    		next_page = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[1]/ul[2]/li/a')[-1].get_attribute("href")
	    	except:
	    		print(url, i)

	    	if url==next_page:   # trang vừa load là trang cuối
	    		break
	    	else:
	    		url = next_page

	    	driver.get(next_page) 
	    	time.sleep(2)

	    	links_ = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[2]/ul/li/div/h4/a") + \
	    			 driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li/div/h4/a")
	    	links_ = [el.get_attribute("href") for el in links_]
	    	links += links_

	    	i+=1
	            
	    return(links)


	def details(self, driver, name_category, url):
		driver.get(url)
		time.sleep(2)

		name_content = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/h1')[0].text
		author = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[1]/p/b')[0].text

		return ([name_category, name_content, url, author])   
    
    
    
if __name__=='__main__':
    wonder = Admicro()
    wonder.get_all()     
