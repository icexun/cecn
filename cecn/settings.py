# Scrapy settings for cecn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cecn'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['cecn.spiders']
NEWSPIDER_MODULE = 'cecn.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = {
    'cecn.pipelines.CecnPipeline': 1000,
}