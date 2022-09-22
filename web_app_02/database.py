import pymongo
from common_method import CommonMethod
from bson.json_util import dumps, loads
import json


MONGODB_URI='mongodb://localhost'
client = pymongo.MongoClient(MONGODB_URI)

def create_database(database):
  databases = client.list_database_names()
  if database not in databases:
    new_database = client[database]
    print('New database created.', new_database)


def create_table(database, collection):
  collections = client[database].list_collection_names()
  if collection not in collections:
    new_collection = client[database][collection]
    print('New collection created', new_collection)


def insert_data(database, collection, record):
  data = client[database][collection].insert_one(record)
  if data:
    return CommonMethod.created_response()
  else:
    return CommonMethod.failed_response()


def find_all(database, collection):
  data = client[database][collection].find()

  users = []
  for user in data:
    users.append(json.loads(dumps(user)))
    
  return CommonMethod.success_response(users)

