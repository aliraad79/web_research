import scrapy


class CafebazaarItem(scrapy.Item):
    package_name = scrapy.Field()
    rating = scrapy.Field()
