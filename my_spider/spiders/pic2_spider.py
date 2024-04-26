# -*- coding: utf-8 -*-
from typing import Iterable
from urllib.request import Request
import scrapy
from my_spider.items import PicItem
from my_spider.pipelines import CustomImagesPipeline

class PicSpider(scrapy.Spider):
    name = 'pic2'
    allowed_domains = ['adult-wiki.net']
    start_urls = 'https://adult-wiki.net/actress/%E7%94%B0%E4%B8%AD%E3%81%AD%E3%81%AD'
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'my_spider.pipelines.CustomImagesPipeline': 1,
        }
    }

    def start_requests(self) -> Iterable[Request]:
        headers = {
            'Referer':'https://adult-wiki.net/',
            'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'Linux',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        for i in range(1):
            url = self.start_urls + '?page='+str(i+1)
            yield scrapy.Request(url=url,headers=headers , callback=self.parse)
    
        

    def parse(self, response):
        # soup = BeautifulSoup(response.text, "lxml")
        imgs = response.xpath('//img[@class="fit lazy"]')
        name = response.xpath('/html/body/div[1]/div[1]/div[5]/div/h1/text()').extract()
        for img in imgs:
            pic_url = img.xpath('@data-original').extract()
            pic_alt = img.xpath('@alt').extract()
            # print('pic url is %s , pic alt is %s' %(pic_url , pic_alt))
            item = PicItem()
            item['image_urls'] = pic_url
            item['image_alt'] = pic_alt
            item['image_name'] = name
            yield item