from pymongo import MongoClient
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
with client:
   db = client.testdb
   cars = db.cars.find()
   print(cars.next())
   print(cars.next())
   print(cars.next())
   cars.rewind()
   print(cars.next())
   print(cars.next())
   print(cars.next())    
   print(list(cars))
