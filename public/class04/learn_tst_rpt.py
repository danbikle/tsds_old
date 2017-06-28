"""
learn_tst_rpt.py

This script should learn from observations in feat.csv

Then it should test its learned models on observations later than the training observations.

Next it should report effectiveness of the models.

Demo:
~/anaconda3/bin/python learn_tst_rpt.py TRAINSIZE=25 TESTYEAR=2015

Above demo will train from 25 years before 2015 and predict each day of 2015
"""

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line args
import sys
if (len(sys.argv) != 3):
  print('You typed something wrong:')
  print('Demo:')
  print("~/anaconda3/bin/python genf.py TRAINSIZE=25 TESTYEAR=2015")
  sys.exit()

# I should get cmd line args:
trainsize     = int(sys.argv[1].split('=')[1])
testyear_s    =     sys.argv[2].split('=')[1]
train_end_i   = int(testyear_s)
train_end_s   =     testyear_s
train_start_i = train_end_i - trainsize
train_start_s = str(train_start_i)
# train and test observations should not overlap:
test_start_i  = train_end_i
test_start_s  = str(test_start_i)
test_end_i    = test_start_i+1
test_end_s    = str(test_end_i)

feat_df  = pd.read_csv('feat.csv')
train_sr = (feat_df.cdate > train_start_s) & (feat_df.cdate < train_end_s)
test_sr  = (feat_df.cdate > test_start_s)  & (feat_df.cdate < test_end_s)
train_df = feat_df[train_sr]
test_df  = feat_df[test_sr]

# I should build a Linear Regression model from slope columns in train_df:
x_train_a = np.array(train_df)[:,3:]
y_train_a = np.array(train_df.pctlead)
from sklearn import linear_model
linr_model = linear_model.LinearRegression()
# I should learn:
linr_model.fit(x_train_a, y_train_a)
# Now that I have learned, I should predict:
x_test_a       = np.array(test_df)[:,3:]
predictions_a  = linr_model.predict(x_test_a)
predictions_df = test_df.copy()
predictions_df['pred_linr'] = predictions_a.reshape(len(predictions_a),1)

# I should build a GBRT Regression model:
from sklearn.ensemble import GradientBoostingRegressor
gbr_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,max_depth=1, random_state=0, loss='ls')
# I should learn:
gbr_model.fit(x_train_a, y_train_a)
# Now that I have learned, I should predict:
x_test_a       = np.array(test_df)[:,3:]
predictions_a  = gbr_model.predict(x_test_a)
predictions_df['pred_gbr'] = predictions_a.reshape(len(predictions_a),1)

# I should build a Logistic Regression model.
logr_model    = linear_model.LogisticRegression()
# I should get classification from y_train_a:
# Should I prefer median over mean?:
# class_train_a = (y_train_a > np.median(y_train_a))
class_train_a = (y_train_a > np.mean(y_train_a))
# I should learn:
logr_model.fit(x_train_a, class_train_a)
# Now that I have learned, I should predict:
predictions_a               = logr_model.predict_proba(x_test_a)[:,1]
predictions_df['pred_logr'] = predictions_a.reshape(len(predictions_a),1)

# I should create a CSV to report from:
predictions_df.to_csv('predictions.csv', float_format='%4.6f', index=False)

# I should report long-only-effectiveness:
eff_lo_f = np.sum(predictions_df.pctlead)
print('Long-Only-Effectiveness:')
print(eff_lo_f)

# I should report Linear-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_linr)
predictions_df['eff_linr'] = eff_sr
eff_linr_f                 = np.sum(eff_sr)
print('Linear-Regression-Effectiveness:')
print(eff_linr_f)

# I should report GBRT-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_gbr)
predictions_df['eff_gbr'] = eff_sr
eff_gbr_f                 = np.sum(eff_sr)
print('GBRT-Regression-Effectiveness:')
print(eff_gbr_f)

# I should report Logistic-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_logr - 0.5)
predictions_df['eff_logr'] = eff_sr
eff_logr_f                 = np.sum(eff_sr)
print('Logistic-Regression-Effectiveness:')
print(eff_logr_f)

import matplotlib
matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt

rgb0_df          = predictions_df[:-1][['cdate','cp']]
rgb0_df['cdate'] = pd.to_datetime(rgb0_df['cdate'], format='%Y-%m-%d')
rgb0_df.columns  = ['cdate','Long Only']
# I should create effectiveness-line for Linear Regression predictions.
# I have two simple rules:
# 1. If blue line moves 1%, then model-line moves 1%.
# 2. If model is True, model-line goes up.
len_i      = len(rgb0_df)
blue_l     = [cp       for cp       in predictions_df.cp]
pred_linr_l = [pred_linr for pred_linr in predictions_df.pred_linr]
linr_l     = [blue_l[0]]
for row_i in range(len_i):
  blue_delt = blue_l[row_i+1]-blue_l[row_i]
  linr_delt = np.sign(pred_linr_l[row_i]) * blue_delt
  linr_l.append(linr_l[row_i]+linr_delt)
rgb0_df['Linear Regression'] = linr_l[:-1]

# I should create effectiveness-line for GBRT Regression predictions.
pred_gbr_l = [pred_gbr for pred_gbr in predictions_df.pred_gbr]
gbr_l     = [blue_l[0]]
for row_i in range(len_i):
  blue_delt = blue_l[row_i+1]-blue_l[row_i]
  gbr_delt = np.sign(pred_gbr_l[row_i]) * blue_delt
  gbr_l.append(gbr_l[row_i]+gbr_delt)
rgb0_df['GBRT Regression'] = gbr_l[:-1]

# I should create effectiveness-line for Logistic Regression predictions.
pred_logr_l = [pred_logr for pred_logr in predictions_df.pred_logr]
logr_l     = [blue_l[0]]
for row_i in range(len_i):
  blue_delt = blue_l[row_i+1]-blue_l[row_i]
  logr_delt = np.sign(pred_logr_l[row_i]-0.5) * blue_delt
  logr_l.append(logr_l[row_i]+logr_delt)
rgb0_df['Logistic Regression'] = logr_l[:-1]

rgb1_df = rgb0_df.set_index(['cdate'])
rgb1_df.plot.line(title="RGB Effectiveness Visualization "+testyear_s, figsize=(11,7))
plt.savefig('rgb.png')
plt.close()

'bye'
