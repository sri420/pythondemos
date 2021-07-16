
import pandas as pd
import awswrangler as wr


df = pd.DataFrame({"id": [1, 2], "value": ["foo", "boo"]})

path1=f"s3://hello-bucket-tn/parquet/dataset/file1.parquet"

wr.s3.to_parquet(df,path1)

print(wr.s3.read_parquet([path1]))
