# corr.py

# For 2016,
# This script should calculate correlation between day1-gain and day2-gain.

import pandas as pd

my_df    = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_pred = my_df['cdate'] > '2016'
sp0_df   = my_df[sp0_pred]
day1g_sr = sp0_df['pctlag1']
day2g_sr = sp0_df['pctlead']

print('For 2016,')
print('Correlation between day1-gain and day2-gain:')
import numpy as np
mycorr = np.corrcoef(day1g_sr, day2g_sr)[0,1]
print(mycorr)

'bye'
