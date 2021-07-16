from pymongo import MongoClient

client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

with client:
  db = client.testdb
  db.cars.drop()
