import scrapy


class NextPageSpider(scrapy.Spider):
    name = 'next_page'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        span_test = response.css("div.quote span.text::text")[0].get()
        yield {"span_text": span_test}

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
