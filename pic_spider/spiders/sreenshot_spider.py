from typing import Iterable
import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
from random import Random
import uuid

class ScreenshotSpider(scrapy.Spider):
    name = 'screenshot'
    start_urls = ['https://scrapy-cookbook.readthedocs.io/' ,
                  'https://scrapy-cookbook.readthedocs.io/zh-cn/latest/scrapy-02.html',
                  'https://scrapy-cookbook.readthedocs.io/zh-cn/latest/scrapy-07.html']

    


    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get(response.url)
        driver.save_screenshot('screenshot-' + str(uuid.uuid4())  + '.png')
        driver.quit()

        yield {
            'url': response.url,
            # 'screenshot_path': '/home/guan/data/selenium'
        }