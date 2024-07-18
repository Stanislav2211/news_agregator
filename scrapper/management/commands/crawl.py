from django.core.management.base import BaseCommand
from scrapper.scrapper.spiders import newsspider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = 'Crawl the news'

    def handle(self,*args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(newsspider.BbcSpider)
        process.crawl(newsspider.HackerNewsSpider)
        process.start()