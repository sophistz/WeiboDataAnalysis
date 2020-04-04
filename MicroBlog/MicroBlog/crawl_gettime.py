from scrapy.spider import Spider,Request
from MicroBlog.items import MicroblogItem
from scrapy.conf import settings
from bs4 import BeautifulSoup
import os.path
import time,datetime
import json
import re
import csv


base_mblog_url = 'http://m.weibo.cn/status/%s'
base_comments_url = "http://m.weibo.cn/api/comments/show?id=%s&page=%s"
base_reposts_url = 'http://m.weibo.cn/api/statuses/repostTimeline?id=%s&page=%s'


class WeiboCrawl(Spider):
    name = 'weiboCrawl'

    def __init__(self,mblog_id=None,*args,**kwargs):
        super(WeiboCrawl, self).__init__(*args,**kwargs)
        self.mblog_url = base_mblog_url % (mblog_id)
        self.max=0

    def start_requests(self):
        yield Request(self.mblog_url,callback=self.parse)

    def parse(self, response):

        pattern = r'var \$render_data = \[((.|\s)*?})\]'
        raw_data = re.search(pattern, response.text)
        raw_data = raw_data.group(1)
        json_data = json.loads(raw_data)

        status = json_data['status']
        items = self.putItem(status)
        yield items
        if status['reposts_count']:
            reposts_url = base_reposts_url % (status['id'], str(1))
            yield Request(reposts_url, callback=self.getReposters)

    def putItem(self,status):
        user_info = status['user']
        items = MicroblogItem()
        items['mblog_id'] = str(status['id'])
        items['mblog_reposts_count'] = int(status['reposts_count'])
        items['mblog_comments_count'] = int(status['comments_count'])
        items['mblog_attitudes_count'] = int(status['attitudes_count'])
        items['mblog_created_at'] = status['created_at']
        try:
            items['mblog_raw_text'] = status['raw_text']
        except:
            items['mblog_raw_text'] = status['text']
        try:
            items['mblog_oid'] = str(status['retweeted_status']['id'])
        except:
            items['mblog_oid'] = str(status['id'])
        try:
            items['mblog_pid'] = str(status['pid'])
        except:
            items['mblog_pid'] = items['mblog_oid']


        items['usr_id'] = str(user_info['id'])
        items['mblog_layer']= 0


        return items

    def getReposters(self,response):

        pattern = 'page=(\d+)'
        result = re.search(pattern, response.url)
        page_id = result.group(1)
        try:
            json_data = json.loads(response.text)
            data = json_data['data']
            reposts_data = data['data']

            if int(page_id)== 1:
                self.max = data['max']

            for item in reposts_data:
                items = self.putItem(item)
                time_url = base_mblog_url % (items['mblog_id'])
                yield Request(url=time_url, meta={"item": items}, callback=self.get_accurate_time)
        except:
            pass

        if int(page_id) < int(self.max):
            reposts_url = re.sub(pattern,'page='+str(int(page_id)+1),response.url)
            yield Request(reposts_url,callback=self.getReposters)

    def get_accurate_time(self, response):

        items = response.meta["item"]
        pattern = r'var \$render_data = \[((.|\s)*?})\]'
        raw_data = re.search(pattern, response.text)
        raw_data = raw_data.group(1)
        json_data = json.loads(raw_data)

        status = json_data['status']
        items['mblog_created_at'] = status['created_at']

        yield items
