import scrapy


class MyScraperItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    pass