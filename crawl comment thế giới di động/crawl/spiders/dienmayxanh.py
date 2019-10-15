# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import scrapy
from CRAWL.items import dienmayxanh_urlItem
from scrapy_splash import SplashRequest


class DMXURLSpider(scrapy.Spider):

    name = "dmxurl"
    start_urls = ['https://www.dienmayxanh.com/dien-thoai']
    
    script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(0.5))
            assert(splash:runjs("$(document.querySelector("#product-list > div > a")).click();"))
            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
        """

# =============================================================================
#     def parse(self, response):
#         for i in range(0,10):
#             yield scrapy.FormRequest.from_response(response=response,
#                                                    formdata={"catid": "42",
#                                                              "catname": "Điện thoại",
#                                                              "caturl": "dien-thoai",
#                                                              "pagesize": "25",
#                                                              "pageidx": str(i+1),
#                                                              "isFilter": "0",
#                                                              "sortby": "0",
#                                                              "manu_80": "0",
#                                                              "manu_2": "0",
#                                                              "manu_1971": "0",
#                                                              "manu_104": "0",
#                                                              "manu_2235": "0",
#                                                             "manu_2236": "0",
#                                                             "manu_17566": "0",
#                                                             "manu_17201": "0",
#                                                             "manu_1": "0",
#                                                             "manu_27": "0",
#                                                             "manu_19": "0",
#                                                             "manu_110": "0",
#                                                             "manu_5332": "0",
#                                                             "manu_2327": "0",
#                                                             "manu_111": "0",
#                                                             "manu_100": "0",
#                                                             "pri_7": "0",
#                                                             "pri_9": "0",
#                                                             "pri_289": "0",
#                                                             "pri_562": "0",
#                                                             "pri_253": "0",
#                                                             "new": "0",
#                                                             "installment0": "0",
#                                                             "shockprice": "0",
#                                                             "pro_62879": "0",
#                                                             "pro_39237": "0",
#                                                             "pro_39238": "0",
#                                                             "pro_140888":"0",
#                                                             "pro_140889": "0",
#                                                             "pro_140890": "0",
#                                                             "pro_140891": "0",
#                                                             "pro_140894": "0",
#                                                             "pro_140895": "0",
#                                                             "pro_140896": "0",
#                                                             "pro_140897": "0",
#                                                             "pro_16430": "0",
#                                                             "pro_9009": "0",
#                                                             "pro_10882": "0",
#                                                             "pro_7759": "0",
#                                                             "pro_19880": "0",
#                                                             "pro_7760": "0",
#                                                             "pro_57280": "0",
#                                                             "pro_57279": "0",
#                                                             "pro_57311": "0",
#                                                             "pro_40434": "0",
#                                                             "pro_40435": "0"},
#                                                    callback=self.parse_item)
# =============================================================================
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse_item)        
            
            
    # load all item in page 
    def parse_item (self, response):
        item = dienmayxanh_urlItem()
        product_list = response.xpath('//*[@id="product-list"]/ul')
        for product_row in product_list:
            product = product_row.xpath('li')
            for data in product:
                try: 
                    item["name"] = data.xpath('div/a/@title').get()
                    item["url"] = 'https://www.dienmayxanh.com/dien-thoai' + data.xpath('div/a/@href').get()
                    yield item
                except:
                    pass
                
        yield SplashRequest(
            url=response.url,
            callback=self.parse,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )
       



                                          
    
        