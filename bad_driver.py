# -*- coding: utf-8 -*-

import plotly.plotly as py
import pandas as pd

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Portfolio"
file_path = p+"/data/bad-drivers-geo.csv"
df = pd.read_csv(file_path)

df['text'] = df['state'] + '<br>Fatal Collisions ' + (df['fatal_collision']).astype(str)+' Drivers per Billion Miles'
limits = [(5, 9),(9, 13),(13, 17),(17, 21),(21, 25)]
colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
cities = []

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['fatal_collision'],
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    cities.append(city)

layout = dict(
        title = '2012 US Fatal Car Collisions<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict( data=cities, layout=layout )
py.iplot( fig, validate=False, filename='bad-drivers' )

