# calc1.py

# This script should calculate lag1 for a time series.

# Here is a simple time series implemented as a simple List:
ts_l = [
  ['2016-01-04', 2012.66]
  ,['2016-01-05', 2016.71]
  ,['2016-01-06', 1990.26]
  ,['2016-01-07', 1943.09]
  ,['2016-01-08', 1922.03]
  ,['2016-01-11', 1923.67]
  ,['2016-01-12', 1938.68]
  ,['2016-01-13', 1890.28]
  ,['2016-01-14', 1921.84]
  ,['2016-01-15', 1880.33]
  ,['2016-01-19', 1881.33]
  ,['2016-01-20', 1859.33]
  ,['2016-01-21', 1868.99]
  ,['2016-01-22', 1906.90]
  ,['2016-01-25', 1877.08]
  ,['2016-01-26', 1903.63]
  ,['2016-01-27', 1882.95]
  ,['2016-01-28', 1893.36]
  ,['2016-01-29', 1940.24]
]

# I start the calculation by getting prices copied into a List:
cp0_l = [el[1] for el in ts_l]

# With a copy of the List,
# I push a value into the top of the List and cut off a value from the bottom:
cp1_l = [cp0_l[0]] + cp0_l[0:-1]

# I should check that the two Lists are same length:
len(cp0_l) == len(cp1_l) # should be True

# I should convert the Lists to Numpy Arrays so I can do arithmetic:
import numpy  as np
cp0_a = np.array(cp0_l)
cp1_a = np.array(cp1_l)
# I should do arithmetic:
lag1_a = cp0_a - cp1_a


# I should use Pandas to visualize the enhanced time series:
import pandas as pd

lag1_df = pd.DataFrame(ts_l)
lag1_df.columns = ['cdate','cp']
lag1_df['lag1'] = lag1_a
print('Here is a time series of prices and a calculation of lag1:')
print(lag1_df)

'bye'
 
