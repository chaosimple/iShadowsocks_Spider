# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class IshadowsocksSpiderPipeline(object):
    def process_item(self, item, spider):
        with open('Result.json', 'w') as ff:
            line = json.dumps(dict(item)) + "\n"
            ff.write(line)
            print 'ok'
        return item