# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    headline = scrapy.Field()
    avatar_url = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    follower_count = scrapy.Field()
    url_token = scrapy.Field()