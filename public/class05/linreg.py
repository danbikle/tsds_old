# linreg.py

# This script should do linear regression.
# Demo:
# python linreg.py

# As of today, allpredictions.csv contains 8955 rows.
# 8900 - 2600 is 6300 is 6300 days is 25 years.
# I should learn from 25 years of data:

import pdb
import pandas as pd
import numpy  as np

csv_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')[2599:8900]

train_df = csv_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']]
train_a  = np.array(train_df)

pdb.set_trace()
csv_df.tail()
train_a[-4:]

x_train_a = train_a[:,1:]
y_train_a = train_a[:,0]

# I should learn from x_train_a,y_train_a:
from sklearn import linear_model
clf_lr = linear_model.LinearRegression()
clf_lr.fit(x_train_a, y_train_a)

# Now that I have learned, I should predict:

'bye'
# 
