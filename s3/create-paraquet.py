import pandas as pd
df = pd.DataFrame(data={'col_1': [2, 3], 'col_2': [4, 5]})
df.to_parquet('df.parquet.gzip',compression='gzip')
