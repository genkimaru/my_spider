from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse
from datetime import date 
import pymysql
from scrapy.exceptions import DropItem
from .settings import MYSQL_SETTINGS
import pdb
class CustomImagesPipeline(ImagesPipeline):

    index = 1
    name = 'default'
    def file_path(self, request, response=None, info=None):
        # image_guid = request.url.split('/')[-1]  # 获取图片的文件名
        filename = self.name +'-'+str(self.index)
        self.index += 1
        # pdb.set_trace()
        path = date.today().strftime('%Y-%m-%d') +'/%s/%s'  % (self.name , filename)
        print(path)
        return path
    

    def process_item(self, item, spider):
        # print(item['image_name'])
        self.name = item['image_name'][0]
        # pdb.set_trace()
        return super().process_item(item, spider)


class DBRankPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(**MYSQL_SETTINGS)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO dbitem (database_name, database_type,current_rank,last_year_rank) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (item['database_name'], item['database_type'] ,item['current_rank'] , item['last_year_rank']))
        return item
