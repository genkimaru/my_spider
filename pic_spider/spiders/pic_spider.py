# -*- coding: utf-8 -*-
import scrapy
from pic_spider.items import PicItem

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['panorama.cn']
    start_urls = ['http://panorama.cn/tupian/meinv.html']
    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    def parse(self, response):
        pic_urls = response.xpath('//*[@id="gallery-list"]/li/a/img/@src').extract()
        for pic_url in pic_urls:
            item = PicItem()
            item['image_urls'] = [pic_url]
            yield item