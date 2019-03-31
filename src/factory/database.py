from pymongo import MongoClient
from bson import ObjectId

from config import config


class Database(object):
    def __init__(self):
        self.client = MongoClient(config['db']['url'])  # configure db url
        self.db = self.client[config['db']['name']]  # configure db name

    def insert(self, element, collection_name):
        inserted = self.db[collection_name].insert_one(element)  # insert data to db
        return str(inserted.inserted_id)

    def find(self, criteria, collection_name, cursor=False):  # find all from db
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])

        found = self.db[collection_name].find(filter=criteria)

        if cursor:
            return found

        found = list(found)

        return found



