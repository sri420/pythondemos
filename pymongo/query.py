from pymongo import MongoClient
import datetime
from pprint import pprint
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")

from dateutil.relativedelta import relativedelta
now=datetime.datetime.now()
ayearback=now + relativedelta(years=-1)
print(now)
print(ayearback)

with client:
   db = client.testdb
   col=db.get_collection('cars')
   response=col.find(
           {
               'dop': { '$lt':ayearback },
               'archivetos3': { '$exists': False } 
            }
        )
   for car in response:
      pprint(car)
