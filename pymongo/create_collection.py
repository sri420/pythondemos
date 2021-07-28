from pymongo import MongoClient
import datetime
cars = [ {'name': 'Audi', 'price': 52642,'dop': datetime.datetime(2020, 7, 29),'archivetos3': True},
         {'name': 'Mercedes', 'price': 57127,'dop':datetime.datetime(2020,7,28)},
         {'name': 'Skoda', 'price': 9000,'dop':datetime.datetime(2020,7, 27), 'archivetos3': True}
        ]
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

with client:
  db = client.testdb
  db.cars.insert_many(cars)
