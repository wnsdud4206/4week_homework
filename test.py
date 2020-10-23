from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

test = list(db.order.find({}, {"_id": False}))
print(test)
# for ts in test:
#     print(ts)