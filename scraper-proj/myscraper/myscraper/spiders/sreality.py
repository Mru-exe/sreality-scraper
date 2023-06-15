import scrapy
from myscraper.items import MyScraperItem


class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    def parse(self, response):
        items = response.css('.property')
        for item in items[:500]:
            title = item.css('div.property ng-scope').get()
            image = item.css('.gallery-img-container img::attr(src)').get()

            scraped_item = MyScraperItem()
            scraped_item['title'] = title
            scraped_item['image'] = image

            yield scraped_item
