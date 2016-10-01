#!/bin/bash

# This script should demo Gradient Boosted Regression Trees (GBRT).
# Ref:
# https://en.wikipedia.org/wiki/Gradient_boosting
# http://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting
# http://scikit-learn.org/stable/modules/ensemble.html#regression

mkdir -p ~/tsds/public/class04/
cd       ~/tsds/public/class04/

# I should get prices from Yahoo:
/usr/bin/curl http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC > gspc.csv

# I should extract two columns and also sort:
echo cdate,cp                                                              > gspc2.csv
sort ~/reg4us/public/csv/gspc.csv|awk -F, '{print $1"," $5}'|grep -v Date >> gspc2.csv
exit

# I should compute features from the prices:
~/anaconda3/bin/python genf.py SLOPES='[2,3,4,5,6,7,8,9]'

# I should learn, test, and report:
~/anaconda3/bin/python learn_tst_rpt.py TRAINSIZE=25 TESTYEAR=2016

exit
