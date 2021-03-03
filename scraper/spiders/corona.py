import scrapy
from scrapy.selector import Selector

class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus']

    def parse(self, response):

        for country in response.xpath("//td/a[@class='mt_a']"):
            url = country.xpath(".//@href").get()
            county_name = country.xpath(".//text()").get()
            yield {
                "country_name":county_name,
                "country_link": url
            }
