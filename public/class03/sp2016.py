# sp2016.py

# This script should create a scatter-plot from 2016 data in allpredictions.csv

import pandas as pd

easier_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_pred  = easier_df['cdate'] > '2016'
sp0_df    = easier_df[sp0_pred]
x_sr      = sp0_df['pctlag1']
y_sr      = sp0_df['pctlead']

import matplotlib.pyplot as plt
plt.scatter(x_sr, y_sr)
plt.show()

'bye'
