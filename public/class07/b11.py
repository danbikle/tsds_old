# b11.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#userguide-charts-scatter-color-groups

import pdb
from bokeh.charts import Scatter, output_file, show
import pandas as pd
yr_i     = 2014
yr_s     = str(yr_i)
feat0_df = pd.read_csv("feat.csv")
feat1_df = feat0_df[['cdate','pctlead','dow','moy']]
cdate_sr = (feat1_df.cdate > yr_s) & (feat1_df.cdate < str(yr_i+1))
feat2_df = feat1_df[cdate_sr]
splot    = Scatter(feat2_df
  ,x     ='moy'
  ,y     ='pctlead'
  ,title =yr_s+' PCT-Lead vs Month of Year'
  ,xlabel=yr_s+' Month of Year'
  ,ylabel="PCT-Lead")#splot

output_file("b11.html")
show(splot)
'bye'

