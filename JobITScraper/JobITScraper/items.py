# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobitscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
    rank = scrapy.Field()
    experience = scrapy.Field()
    number_of_recruits = scrapy.Field()
    working_form = scrapy.Field()
    sex = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    requirements = scrapy.Field()
    benefit = scrapy.Field()
    url = scrapy.Field()
    