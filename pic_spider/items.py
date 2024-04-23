# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# -*- coding: utf-8 -*-
import scrapy

class PicItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
