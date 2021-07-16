import pandas as pd
csvdf=pd.read_csv('hello.csv')
print(csvdf)
csvdf.to_parquet('myfile.parquet', engine='fastparquet')
pd.read('myfile.paraquet')
        
