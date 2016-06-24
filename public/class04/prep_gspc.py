# prep_gspc.py

# This script should prep /tmp/gspc_train.csv and /tmp/gspc_test.csv for tf021.bash

# Demo:
# python prep_gspc.py

import numpy  as np
import pandas as pd
import pdb

# I should use Pandas and Numpy here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df['cdate'] > '2000') & (data_df['cdate'] < '2016')
test_sr  =  data_df['cdate'] > '2016'
train_df = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]

pdb.set_trace()
test_df.tail()

'bye'
