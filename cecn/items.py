# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CecnItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pdate = Field()
    author = Field()
    title = Field()
    subtitle = Field()
    body = Field()

