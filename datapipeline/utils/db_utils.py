import pymongo
from pymongo import collection

from datapipeline.app_conf import MONGO_URL, DB_NAME

db_client = pymongo.MongoClient(MONGO_URL)
crypto_db = db_client[DB_NAME]

def get_records(collection_name, query, projection=None):
    records = []
    collection = crypto_db[collection_name]
    count = collection.count_documents(query)
    if(count):
        records = collection.find(query, projection)
    return records

def insert_single_record(collection_name, record):
    print("Update single record")
    collection = crypto_db[collection_name]
    result = collection.insert_one(record)
    return result

def insert_multiple_record(collection_name, records):
    print("Update multiple records")
    collection = crypto_db[collection_name]
    result = collection.insert_many(records)
    return result