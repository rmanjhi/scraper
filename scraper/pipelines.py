# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from .settings import *


class ScraperPipeline:

    def __init__(self):
        connection = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
        db = connection[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]

    def process_item(self, item, spider):

        self.collection.insert(dict(item))

        return item
