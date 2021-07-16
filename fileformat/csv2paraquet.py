import pandas as pd

def write_parquet_file():
    df = pd.read_csv('data/us_presidents.csv')
    df.to_parquet('tmp/us_presidents.parquet')


write_parquet_file()
