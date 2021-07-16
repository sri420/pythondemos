from datetime import date
import awswrangler as wr
import pandas as pd

import getpass
bucket = getpass.getpass()
path = f"s3://{bucket}/dataset2/"

df = pd.DataFrame({
        "id": [1, 2],
            "value": ["foo", "boo"],
                "date": [date(2020, 1, 1), date(2020, 1, 2)]
                })

wr.s3.to_parquet(
            df=df,
                path=path,
                    dataset=True,
                        mode="overwrite",
                            partition_cols=["date"]
                            )

wr.s3.read_parquet(path, dataset=True)


# wr.s3.to_parquet(
  #          df=df,
   #             path=path,
   #                 dataset=True,
   #                     mode="overwrite"
   #                     )

# wr.s3.read_parquet(path, dataset=True)
