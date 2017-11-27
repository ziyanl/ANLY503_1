# -*- coding: utf-8 -*-

import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
import pandas as pd
import plotly.graph_objs as go

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path = p+"/data/ppg2008.csv"
df = pd.read_csv(file_path, index_col=0)

# Normalize the data columns and sort.
nba = (df - df.mean()) / (df.max() - df.min())
nba.sort('PTS', inplace=True)

score = []
for x in nba.apply(tuple):
  score.extend(x)


data = [
    go.Heatmap(
        z=score,
        x=list(nba.index) * len(nba.columns),
        y=[item for item in list(nba.columns) for i in range(len(nba.index))],
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='NBA Players Statistics, 2012',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='nba-players')


