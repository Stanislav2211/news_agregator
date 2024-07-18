# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from news.models import BBC,HackerNews
'''
class ScrapperPipeline(BaseItemPipeline):
    @sync_to_async
    def process_item(self, item, spider):
        item.save()
        return item

'''
class BbcPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'bbcspider':
            item = BBC(**ItemAdapter(item).asdict())
            item.save()
            yield item
        return item

class HackerNewsPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'hacker':
            item = HackerNews(**ItemAdapter(item).asdict())
            item.save()
            yield item
        return item
