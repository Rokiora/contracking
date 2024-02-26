# database.py
import pymongo

class Database:
# collect connection information
    def __init__(self, uri, dbname, collection_name):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db[collection_name]

# insert one method
    def insert_client(self, client_data):
        self.collection.insert_one(client_data)

        

# update method will go here
