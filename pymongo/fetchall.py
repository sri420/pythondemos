from pymongo import MongoClient
from pprint import pprint
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")


with client:
   db = client.testdb
   col=db.get_collection('cars')
   response=col.find( { } ).sort('dop',-1)
   for car in response:
      pprint(car)
