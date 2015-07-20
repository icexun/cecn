__author__ = 'ice'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
import re

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
       sel = Selector(response)
       comments = sel.xpath('//comment()')
       items = []
       for site in sites:
           item = CecnItem()
           item['pdate'] = re.findall(r'<founder-date>[.]+<]')
           item['author'] = site.xpath('a/@href').extract()
           item['title'] = site.xpath('text()').extract()
           item['body'] =
           items.append(item)
       return items