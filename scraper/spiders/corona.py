import scrapy
from scrapy.selector import Selector
from scraper.items import ScraperItem


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus']

    def parse(self, response):
        data = ScraperItem()
        for country in response.xpath("//td/a[@class='mt_a']"):
            data['country_name'] = country.xpath(".//text()").get()
            data['country_link'] = country.xpath(".//@href").get()
            yield data
