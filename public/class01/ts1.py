# ts1.py

# This script should plot a time series of prices.

import pandas as pd
import datetime

my_df    = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_pred = my_df['cdate'] > '2016'
sp0_df   = my_df[sp0_pred]
cdate_sr = sp0_df['cdate']
cp_sr    = sp0_df['cp']
  
# matplotlib likes dates:
cdate_l = [datetime.datetime.strptime(row, "%Y-%m-%d") for row in cdate_sr]

import matplotlib.pyplot as plt
# cdate_l holds x values, cp_sr: y values
plt.plot(cdate_l, cp_sr)
plt.show()
'bye'
