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
print(data);

# Drop _id column in dataframe
data=data.drop(columns='_id')

# Export dataframe data to csv file ,excluding index
newdatacsv=data.to_csv('hello1.csv',index=False)

# Export dataframe data to json fie, in records orientation
newdatajson=data.to_json('hello2.json',orient='records')

# Display dataframe data
print(newdatacsv);
print(newdatajson);

# Set the path to file in S3
path1=f"s3://hello-bucket-tn/mongodata/cars.parquet"

jsonpath=f"s3://hello-bucket-tn/mongodata/hello2.json"

# Write the data to S3 in Parquet Format
wr.s3.to_parquet(data,path1)

wr.s3.to_json(data,path=jsonpath,orient='records')

csvpath=f"s3://hello-bucket-tn/mongodata/mycsv.csv"

wr.s3.to_csv(data,path=csvpath,index=False)

# Read and Display the S3 data in Parquet Format
print(wr.s3.read_parquet([path1]))
