# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from news.models import BBC,HackerNews

class BbcItem(DjangoItem):
    django_model = BBC

class HackerNewsItem(DjangoItem):
    django_model = HackerNews
