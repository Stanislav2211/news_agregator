import scrapy
from ..items import BbcItem, HackerNewsItem
from news.models import BBC, HackerNews
import re

class BbcSpider(scrapy.Spider):
    name = 'bbcspider'
    allowed_domains = ['bbc.com']
    start_urls = [
        "https://www.bbc.com/news"
    ]

    def parse(self, response):
        article_links = response.css('a[href*="/news/articles/"]::attr(href)').getall()

        for link in article_links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        item = BbcItem()
        item['title'] = response.css('h2::text').get()
        item['article'] = response.css('.sc-4fedabc7-3::text').get()
        item['url'] = response.url
        yield item
           


class HackerNewsSpider(scrapy.Spider):
    name = 'hacker'
    allowed_domains = ['news.ycombinator.com']
    start_urls = [
        'https://news.ycombinator.com/'
    ]

    def parse(self, response):
        elements = response.xpath("//table[@id='hnmain']//tr[@class='athing']")
        for element in elements:
            item = HackerNewsItem()
            item['title'] = element.xpath(".//td[@class='title']/span[@class='titleline']/a/text()").get()
            item['points'] = element.xpath("./following-sibling::tr[1]//span[@class='score']/text()").get()
            item['url'] = element.xpath(".//td[@class='title']/span[@class='titleline']/a/@href").get()
            item['author'] = element.xpath(".//td[@class='title']/span[@class='titleline']/a/text()").get()
            yield item
        
        
