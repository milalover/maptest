# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


import pandas as pd
import geopandas
import geoplot
from shapefilereader import shapefilereader # get shapefilereader from link above and make sure you're using Python 2

import numpy as np
from geopandas.tools import sjoin
import fiona


world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)

# oceans and seas shapefile
#oceans = shapefilereader('World_Seas_IHO_v3.zip')
#oceans = oceans.assign(featurecla = 'Ocean')[['NAME','geometry','featurecla']]\.rename(columns={'NAME':'name'}) 

balts = shapefilereader("iho.zip")
#finland = balts.assign(name='Gulf of Finland')[[]]
#geoplot.choropleth(
#    world, hue=world['gdp_md_est'] / world['pop_est'],
#    cmap='Greens', figsize=(8, 4)
#)

#ocean_test = geoplot.choropleth(
#    oceans, hue=world['gdp_md_est'] / world['pop_est'],
#    cmap='Greens', figsize=(8, 4)
#)

baltic_test = geoplot.choropleth(
    balts, hue=world['gdp_md_est'] / world['pop_est'],
    cmap='Greens', figsize=(8, 4)
)
#finland_test = geoplot.choropleth(
#    finland, hue=world['gdp_md_est'] / world['pop_est'],
#    cmap='Greens', figsize=(8, 4)
#)

#ocean_test #display map
#baltic_test

#baltic_test.to_file("baltic.geojson", driver='GeoJSON')

#Try to webhost
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title="MapsTest"

app.layout = html.Div(children=[
    html.H1("MAPS"),
    dcc.Graph(
        id='baltic',
        figure=baltic_test
    ),
    html.Div([
            html.P('Test Text')])
    ]
)
