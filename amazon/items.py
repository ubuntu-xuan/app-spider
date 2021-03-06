# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #images = scrapy.Field()

    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    body = scrapy.Field()


    #QA
    product = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()


    #Description
    productname = scrapy.Field()
    description = scrapy.Field()



