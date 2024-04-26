# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# -*- coding: utf-8 -*-
import scrapy

class PicItem(scrapy.Item):
    image_urls = scrapy.Field()
    image_alt = scrapy.Field()
    image_name = scrapy.Field()
    images = scrapy.Field()


class DBItem(scrapy.Item):
    database_name = scrapy.Field()
    current_rank  = scrapy.Field()
    last_year_rank = scrapy.Field()
    database_type = scrapy.Field()