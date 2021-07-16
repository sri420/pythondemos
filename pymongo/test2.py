import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://Trustwhere4u:Trustwhere4u@mymongocluster.cyhjc.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
#client.server_info()
db = client.testdb

carscollection=db.cars

import awswrangler as wr
import pandas as pd

# Load Mongo Response to dataframe
data=pd.DataFrame(list(carscollection.find()))
#print(data);

# Drop _id column in dataframe
data=data.drop(columns='_id')


# Declare a list that is to be converted into a column
#address = ['Delhi', 'Bangalore', 'Chennai', 'Patna','Beijing','Peking','Katmandu','Parsipanny','Randolph','Surt','a','b','v''t','5','cairi','cdfd']

#data['name'] = address
#data=data[['prices']] 

#data.insert(2, "Age", [21, 23, 24, 21,22,23,24,25,23,9,9,9,9,9,9,9], True)
# Export dataframe data to csv file ,excluding index
#newdatacsv=data.to_csv('mycsv.csv',index=False)

# Export dataframe data to json fie, in records orientation
#newdatajson=data.to_json('myjson.json',orient='records',lines=True)

# Display dataframe data
#print(newdatacsv);
#print(newdatajson);

# Set the path to file in S3
path1=f"s3://hello-bucket-tn/mongodata/cars.parquet"

jsonpath=f"s3://hello-bucket-tn/mongodata/hello2.json"

# Write the data to S3 in Parquet Format
wr.s3.to_parquet(data,path1,index=False)

#data.reset_index(drop=True,inplace=True)
#print(data)
#data.to_parquet('df.parquet',engine='pyarrow',index=False) 

#wr.s3.to_json(data,path=jsonpath,orient='records')

#csvpath=f"s3://hello-bucket-tn/mongodata/mycsv.csv"

#wr.s3.to_csv(data,path=csvpath,index=False)

# Read and Display the S3 data in Parquet Format
print(wr.s3.read_parquet([path1]))

#print(pd.read_parquet('df.parquet'))
