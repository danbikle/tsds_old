# moy_hist.py

# This script should create a visualization of pctlead vs Month of Year AKA moy:

# I should get dates and prices.

import pandas as pd
import pdb

df10 = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')

# I should compute pctlead:
df10['pctlead'] = (100.0 * (df10.Close.shift(1) - df10.Close) / df10.Close).fillna(0)

# I should compute moy:
dt_sr = pd.to_datetime(df10.Date)
moy_l = [int(dt.strftime('%-m')) for dt in dt_sr]
df10['moy'] = moy_l

# Over the past 30 years I should collect pctlead vs moy:
yr30_i = 252 * 30
df11   = df10[1:yr30_i][['pctlead','moy']]
df11.columns = ['Pct-Lead-Sum','Month-of-Year']

# I should groupby moy and compute mean:
moy_gb = df11.groupby('Month-of-Year')
moy_gb_df = moy_gb.sum()
print(moy_gb_df)

import matplotlib
# matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt

moy_gb_df.plot.bar(title="30 Year Pct-Lead-Sum vs Month-of-Year", figsize=(11,7))
plt.grid(True)
# plt.savefig('pctlead_moy.png')
plt.show()
# plt.close()

'bye'
