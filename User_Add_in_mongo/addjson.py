import json
from  pymongo import MongoClient

with open('users.json') as f:
    record  = json.load(f)

client = MongoClient()
db = client.users

db.users.insert(record)
