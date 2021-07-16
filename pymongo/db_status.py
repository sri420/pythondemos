from pymongo import MongoClient
from pprint import pprint

client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

with client:
  db = client.testdb
  print(db.list_collection_names())
  status = db.command("dbstats")
  pprint(status)
