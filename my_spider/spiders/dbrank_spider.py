import scrapy
# from ..items import DBItem

class DatabaseRankingSpider(scrapy.Spider):
    name = 'rank'
    start_urls = ['https://db-engines.com/en/ranking']

    custom_settings = {
        'ITEM_PIPELINES' : {
            'my_spider.pipelines.DBRankPipeline': 1,
        }
    }

    def parse(self, response):
        for row  in response.xpath('//table[@class="dbi"]//tr[position() > 3]'):
            current_rank = row.xpath('td[1]/text()').get()
            last_year_rank = row.xpath('td[3]/text()').get()
            database_name = row.xpath('th[1]/a/text()').get()
            database_type = row.xpath('th[2]/a/text()').get()

            yield {
                'database_name': database_name,
                'current_rank': current_rank,
                'last_year_rank': last_year_rank,
                'database_type': database_type
            }