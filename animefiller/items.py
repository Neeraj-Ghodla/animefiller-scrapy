# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimefillerItem(scrapy.Item):
    # define the fields for your item here like:
    anime = scrapy.Field()
    number = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    date = scrapy.Field()
