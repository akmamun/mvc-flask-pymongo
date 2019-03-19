from pymongo import MongoClient

from config import config

class Database(object):
    def __init__(self):
        self.client = MongoClient(config['db']['url']) #configure db url
        self.db = self.client[config['db']['name']]  #configure db name


    def insert(self, element, collection_name):
        inserted = self.db[collection_name].insert_one(element)
        return str(inserted.inserted_id)




