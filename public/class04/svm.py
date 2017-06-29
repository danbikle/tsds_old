"""
svm.py

This script is a simple demo of using scikit-learn to run SVM.

Demo:
python svm.py
"""

import pandas as pd
import numpy  as np
import pdb
from sklearn.svm import SVC


# I should use Pandas here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df['cdate'] > '1990') & (data_df['cdate'] < '2016')
test_sr  =  data_df['cdate'] == '2017-06-26'
train_df = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]
train_a       = np.array(train_df)
x_train_a     = train_a[:,1:]
y_train_a     = train_a[:,0]
# I should set the class boundry at 0.0 rather than median of y_train_a:
label_train_a = y_train_a > 0.0
