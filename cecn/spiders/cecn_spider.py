#coding=utf-8

__author__ = 'ice'


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import re
import sys


from cecn.items import CecnItem


class CecnSpider(CrawlSpider):
   name = "cecn"
   allowed_domains = ["paper.ce.cn"]
   start_urls = [
       "http://paper.ce.cn/jjrb/html/2015-07/20/node_2.htm"
   ]

   rules = (
       Rule(SgmlLinkExtractor(allow=('node_', ))),
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
           c = re.search(r'<founder-title>(.*)</founder-title>', comment)
           if (c != None):
                item['title'] = c.group(1)
           #item['pdate'] = comment.select('//founder-date/text()')
           #item['author'] = comment.select('//founder-author/text()')
           #item['title'] = comment.select('//founder-title/text()')
           #item['body'] = sel.select('//founder-content/text()')
           #items.append(item)
       item['body'] = "\n".join(sel.select('//founder-content/p/text()').extract())
       items.append(item)
       return items