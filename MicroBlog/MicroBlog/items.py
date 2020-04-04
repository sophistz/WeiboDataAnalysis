# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MicroblogItem(scrapy.Item):
    # define the fields for your item here like:

    mblog_id = scrapy.Field()
    mblog_created_at = scrapy.Field()
    mblog_reposts_count = scrapy.Field()
    mblog_comments_count = scrapy.Field()
    mblog_attitudes_count = scrapy.Field()
    mblog_raw_text = scrapy.Field()

    usr_id = scrapy.Field()
    mblog_layer = scrapy.Field()


    mblog_pid = scrapy.Field()
    mblog_oid = scrapy.Field()
    pass
