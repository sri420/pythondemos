from pymongo import MongoClient
from pymongo import UpdateOne
from pprint import pprint
from bson.objectid import ObjectId
import datetime
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

with client:
  db = client.testdb
  col=db.get_collection('cars')
  requests = [ UpdateOne( { '_id': ObjectId('61019ed7d203f8b969997ece')  }, {'$set': {'archivetos3': False}}) ]
  result = col.bulk_write(requests)
      
  pprint(result.bulk_api_result)

