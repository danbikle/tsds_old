# hm14.py

# Ref:
# http://bokeh.pydata.org/en/latest/docs/gallery/heatmap_chart.html

# Demo:
# ~/anaconda3/bin/python hm14.py

import pandas as pd

from bokeh.charts   import HeatMap, bins, output_file, show
from bokeh.layouts  import column, gridplot
from bokeh.palettes import RdYlGn6, RdYlGn9

import pdb

yr_i     = 2010
yr_s     = str(yr_i)
feat0_df = pd.read_csv("feat.csv")
feat1_df = feat0_df[['cdate','pctlead','dow','moy']]
#cdate_sr = (feat1_df.cdate > yr_s) & (feat1_df.cdate < str(yr_i+1))
cdate_sr = (feat1_df.cdate > yr_s)
feat2_df = feat1_df[cdate_sr]
tools_s  = 'box_zoom,box_select,crosshair,resize,reset,save,help'

hm0 = HeatMap(feat2_df
              ,x     =bins('dow')
              ,y     =bins('moy')
              ,values='pctlead'
              ,stat  ='mean'
              ,width=900
              ,plot_height=500
              )

output_file("hm14.html", title="Bokeh heatmap example (hm14.py)")

# 

show(hm0)

'bye'
