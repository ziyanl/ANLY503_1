# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
from bokeh.plotting import *
from bokeh.models import HoverTool
from collections import OrderedDict

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path = p+"/data/LAPD_Calls_for_Service_2016.csv"
df = pd.read_csv(file_path)
# filter data with "507P" call type code: noise violation call on a party
sub = df.loc[df['Call Type Code'] == '507P']

sub2 = sub["Dispatch Date"]
sub2 = sub2.groupby(sub["Dispatch Date"]).count()
sub2.to_csv("count.csv")

p2 = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path2 = p2+"/count.csv"
df2 = pd.read_csv(file_path2, names=["Dispatch Date", "Count"])

#count1=df2['Count'].tolist()

# add a column with day of the week
df2['Dispatch Date'] = pd.to_datetime(df2['Dispatch Date'])
df2['day_of_week'] = df2['Dispatch Date'].dt.weekday_name
# add a column with start of the week
df2['week'] = [(date - datetime.timedelta(days=date.dayofweek)).strftime("%Y-%m-%d") for date in df2["Dispatch Date"]]
df2=df2.drop('Dispatch Date', axis=1)

# create a matrix
# columns are day of the week and rows are start date of the week
data = df2.pivot(index='week', columns='day_of_week', values='Count')
data = data.fillna(value=0)

data.to_csv("pivot.csv")

p3 = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path3 = p3+"/pivot.csv"
df2 = pd.read_csv(file_path3, index_col=0)

count = []
for x in df2.apply(tuple):
  count.extend(x)

data = {
  'Start of Week': list(df2.index) * len(df2.columns),
  'Day of Week':  [item for item in list(df2.columns) for i in range(len(df2.index))],
  'Count': count,
}

hover = HoverTool(
        tooltips=[
            ("Count", "@Count"),
        ]
    )  
 
output_file('party_disturbance_la.html')
hm = HeatMap(data, x='Start of Week', y='Day of Week', values='Count', title='\"Party\" Disturbance Calls in LA, 2016', stat=None, tools=[hover], plot_height=300, plot_width=1200)

show(hm)


