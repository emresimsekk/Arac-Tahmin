# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    
    model = scrapy.Field()
    yil = scrapy.Field()
    km = scrapy.Field()
    renk = scrapy.Field()
    fiyat = scrapy.Field()
    il = scrapy.Field()
    pass
