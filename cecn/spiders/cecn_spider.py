#!/usr/bin/python
# coding=utf-8

__author__ = 'ice'


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
import datetime

<<<<<<< HEAD
=======

>>>>>>> bugfix
from cecn.items import CecnItem

global crawl_days, url_list
crawl_days = 1500
url_list = []

#no good way to crawl every days node html link, so generate for days want to collect
def gen_start_urls():
    dt = datetime.datetime.now()

    for i in range(crawl_days):
        y = str(dt.year)
        m = str(dt.month)
        if (len(m) < 2):
            m = '0' + m
        d = str(dt.day)
        if (len(d) < 2):
            d = '0' + d
        dt_str = y + '-' + m + '/' + d
        url_list.append("http://paper.ce.cn/jjrb/html/" + dt_str + "/node_2.htm")
        dt = dt - datetime.timedelta(days=1)
        i = i + 1
    return url_list


class CecnSpider(CrawlSpider):
   name = "cecn"
   allowed_domains = ["paper.ce.cn"]

   print url_list
   #start_urls = gen_start_urls()

<<<<<<< HEAD
   start_urls = [
       "http://paper.ce.cn/jjrb/html/2015-07/20/node_2.htm"
   ]
=======
   #debug
   #start_urls = [
   #    "http://paper.ce.cn/jjrb/html/2015-07/06/node_2.htm"
   #]
>>>>>>> bugfix

   rules = (
       Rule(SgmlLinkExtractor(allow=('node_', ))),
       Rule(SgmlLinkExtractor(allow=('"#"', ))),
       Rule(SgmlLinkExtractor(allow=('content_', )), callback = 'parse_item'),
   )

   def parse_item(self, response):
       sel = HtmlXPathSelector(response)
       comments = sel.select('//comment()').extract()
       items = []
       for comment in comments:
           item = CecnItem()
           #print comment
           # search date, author, and title from comments which lie on the end of html page
           c = re.search(r'<founder-date>(.*)</founder-date>', comment)
           if (c != None):
                item['pdate'] = c.group(1)
           c = re.search(r'<founder-author>(.*)</founder-author>', comment)
           if (c != None):
                item['author'] = c.group(1)
                #print item['author']
           c = re.search(r'<founder-title>(.*)</founder-title>', comment)
           if (c != None):
                item['title'] = c.group(1)
<<<<<<< HEAD
           c = re.search(r'<founder-subtitle>(.*)</founder-subtitle>', comment)
           if (c != None):
                item['subtitle'] = c.group(1)
                print item['subtitle']
=======
                #print item['title']
           c = re.search(r'<founder-subtitle>(.*)</founder-subtitle>', comment)
           if (c != None):
                item['subtitle'] = c.group(1)

>>>>>>> bugfix
       item['body'] = "\n".join(sel.select('//founder-content/p/text()').extract())
       items.append(item)
       return items