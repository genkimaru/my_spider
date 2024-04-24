from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse
from datetime import date 

class CustomImagesPipeline(ImagesPipeline):

    index = 1
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]  # 获取图片的文件名
        filename = 'pic'+str(CustomImagesPipeline.index)
        CustomImagesPipeline.index += 1
        path = date.today().strftime('%Y-%m-%d') +'/%s' % (filename)
        print(path)
        return path
