import awswrangler as wr
import pandas as pd
wr.s3.to_parquet(
       df=pd.DataFrame({'col': [1, 2, 3],'col2': ['A', 'A', 'B']}),
       path='s3://hello-bucket-tn/prefix',
       dataset=True,
       partition_cols=['col2']
       )
