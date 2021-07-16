import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
       object_name = file_name

    s3_client = boto3.client('s3')
    try:
          response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
           logging.error(e)
           return False
    return True

import pandas as pd
df = pd.DataFrame(data={'col_1': [2, 3], 'col_2': [4, 5]})
df.to_parquet('df.parquet',compression='gzip')

upload_file("df.parquet","hello-bucket-tn","my-paraquet-file")
