# linreg.py

# This script should do linear regression.
# Demo:
# python linreg.py

# As of today, allpredictions.csv contains 8955 rows.
# 8900 - 2600 is 6300 is 6300 days is 25 years.
# I should learn from 25 years of data:

import pdb
import pandas as pd

csv_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')[2599:8900]
pdb.set_trace()
csv_df.head()
csv_df.tail()

'bye'
# 
