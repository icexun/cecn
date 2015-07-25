# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class CecnPipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect('localhost','root', 'root', 'cecn', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

  def process_item(self, item, spider):
    #print item['body']
    try:
        #self.cursor.execute("TRUNCATE TABLE paper ")
        self.cursor.execute("""INSERT INTO paper (pdate, author, title, subtitle, body)
<<<<<<< HEAD
                        VALUES (%s, %s, %s, %s)""",
=======
                        VALUES (%s, %s, %s, %s, %s)""",
>>>>>>> bugfix
                       (item['pdate'],
                        item['author'].encode('utf-8'),
                        item['title'].encode('utf-8'),
                        item['subtitle'].encode('utf-8'),
                        item['body'].encode('utf-8')))

        self.conn.commit()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    return item

