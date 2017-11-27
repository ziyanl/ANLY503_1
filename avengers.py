# -*- coding: utf-8 -*-

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from collections import OrderedDict
import pandas as pd

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path = p+"/data/avengers.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

name = df['Name/Alias'].tolist()
year = df['Years since joining'].tolist()
appearance = df['Appearances'].tolist()
current = df['Current?'].tolist()
honorary = df['Honorary'].tolist()

source = ColumnDataSource(
        data=dict(
            name = name,
            year = year,
            appearance = appearance,
            current = current,
            honorary = honorary
        )
    )

hover = HoverTool(
        tooltips=[
            ("Name", "@name"),
            ("Year since joining", "@year"),
            ("Appearance", "@appearance"),
            ("Current?", "@current"),
            ("Honorary", "@honorary")
        ]
    )

# manually map color to honorary status
color_list = []
for h in honorary:
    if h == 'Full':
        color_list.append('orange')
    elif h == 'Academy':
        color_list.append('#B3DE69')
    elif h == 'Probationary':
        color_list.append('red')
    else:
        color_list.append('blue')   

p = figure(plot_width=800, plot_height=600, tools=[hover],
           title="Avengers Years vs Appearances, marked by Honorary Status")

p.scatter('year', 'appearance', line_color=None, fill_color = color_list, size=6, source=source)
p.xaxis.axis_label = "Years since joining"
p.yaxis.axis_label = "Appearances"
p.legend.location = "top_left"

output_file("avengers.html")

show(p)

