# sp2016.py

# This script should create a scatter-plot from 2016 data in allpredictions.csv

import pandas as pd
import pdb

easier_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_pred  = easier_df['cdate'] > '2016'
sp0_df    = easier_df[sp0_pred]
pdb.set_trace()

sp1_df = sp0_df[['pctlag1','pctlead']]

sp0_df.tail()
sp1_df.tail()



'bye'
