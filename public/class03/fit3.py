# fit3.py

# This script should use NumPy and scikit-learn to fit a line to three points.

import numpy as np
import pdb

pdb.set_trace()

# I should declare three points:
pt0 = [0.001,0.001]
pt1 = [1.1,1.1]
pt2 = [2.2,2.2]

# I should get the x,y values from the points:
x_l = [pt0[0],pt1[0],pt2[0]]
y_l = [pt0[1],pt1[1],pt2[1]]

# I should access scikit-learn.
# Ref:
# http://scikit-learn.org/stable/modules/linear_model.html
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

from sklearn import linear_model

# I should create linear regression object:
regr = linear_model.LinearRegression()



'bye'
