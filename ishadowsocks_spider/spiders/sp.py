#!/usr/bin/env python
#coding:utf-8
"""
  Author : Chaos--<chaosimpler@gmail.com>
  Purpose: 
  Created: 2016/1/10
"""
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from ishadowsocks_spider.items import IShadowsocksSpiderItem

########################################################################
class SSSpider(BaseSpider):
    """"""
    name = 'SSSpider'
    allowed_domains = ["ishadowsocks.com"]
    start_urls = [
    "http://www.ishadowsocks.com/"
    ]
    
    
    #----------------------------------------------------------------------
    def parse(self,response):
        """
        
        """
        ss=response.xpath('//section[@id="free"]/div/div/div[@class="col-lg-4 text-center"]')
        si=IShadowsocksSpiderItem()
        for s in ss:
            si['Server']=s.xpath('h4/text()').extract()[0].split(":")[1]
            si['Port']=s.xpath('h4/text()').extract()[1].split(":")[1]
            si['Password']=s.xpath('h4/text()').extract()[2].split(":")[1]
        yield si    
    

if __name__ == '__main__':
    print 'test'