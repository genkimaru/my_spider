# -*- coding: utf-8 -*-
from typing import Iterable
from urllib.request import Request
import scrapy
from pic_spider.items import PicItem
from pic_spider.pipelines import CustomImagesPipeline

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['panorama.cn']
    start_urls = 'http://panorama.cn/tupian/'
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'pic_spider.pipelines.CustomImagesPipeline': 1,
        }
    }

    def start_requests(self) -> Iterable[Request]:
        for i in range(1, 3):
            url = self.start_urls + 'meinv-' + str(i) + '--1-v.html'
            yield scrapy.Request(url=url , callback=self.parse)
        
        

    def parse(self, response):
        pic_urls = response.xpath('//*[@id="gallery-list"]/li/a/img/@src').extract()
        for pic_url in pic_urls:
            item = PicItem()
            item['image_urls'] = [pic_url]
            yield item