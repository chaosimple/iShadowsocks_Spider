# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IshadowsocksSpiderPipeline(object):
    def process_item(self, item, spider):
        with open('Result.txt', 'w') as ff:
            ff.write('Server   : ' + item['Server']+"\n")
            ff.write('Port     : '+item['Port']+"\n")
            ff.write('Password : '+item['Password'])
            print 'ok'
        return item
