# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import json
import os


class AnimefillerPipeline:
    def __init__(self):
        # self.conn = pymongo.MongoClient('localhost', 27017)
        self.conn = pymongo.MongoClient(os.environ.get("MONGO_URI"))
        self.db = self.conn["animefillers"]
        self.collection = self.db["episodes"]
        self.data = list()  # it will eventually hold all the data

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item

    def close_spider(self, spider):
        self.collection.insert_many(self.data)
