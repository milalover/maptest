# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Webhost
from IPython.display import IFrame

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import geopandas
import geoplot
from shapefilereader import shapefilereader # get shapefilereader from link above and make sure you're using Python 2


#World file has columns with information in them used to color maps.
world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)

#All Oceans
#http://www.marineregions.org/gazetteer.php?p=browser&id[]=2139&id[]=2145#focus
#?
oceans = shapefilereader('World_Seas_IHO_v3.zip')
oceans = oceans.assign(featurecla = 'Ocean')[['NAME','geometry','featurecla']]\
.rename(columns={'NAME':'name'}) 

#Baltic ocean
balts = shapefilereader("iho.zip")

#Finnish Dataset
#sns.set(style=”whitegrid”, palette=”pastel”, color_codes=True)
#sns.mpl.rc(“figure”, figsize=(10,6))

shp_path = 'shapet/shapet/maakunnat2021_100000.shp'
finland = geopandas.read_file(shp_path)


world_temp = geoplot.choropleth(
    world, hue=world['pop_est'],
    cmap='Greens', figsize=(8, 4)
)

ocean_test = geoplot.choropleth(
    oceans, hue=world['gdp_md_est'] / world['pop_est'],
    cmap='Greens', figsize=(8, 4)
)

baltic_test = geoplot.choropleth(
    balts, hue=world['gdp_md_est'] / world['pop_est'],
    cmap='Greens', figsize=(8, 4)
)

finland_test = geoplot.choropleth(
    finland, hue=world['pop_est'],
    cmap='Greens', figsize=(8, 4)
)

fin = finland.plot()


#ocean_test
#baltic_test
#finland_test

#WEBHOST:
    
app = dash.Dash(__name__)
server = app.server
app.title="MapsTest"

app.layout = html.Div(children=[
    html.H1("MAPS"),
    #dcc.Dropdown(id="value-selected", value='pop_est', options=[{'label': "Population ", 'value': 'pop_est'}, {'label': "GDP Per Capita ", 'value': 'gdp_md_est'}]),
    dcc.Graph(
        id='map'
    ),
    html.Div([
            html.P('Test Text')]),
   dcc.Input(id='inp', value='', type='text'),
   html.Div(id='out-div')
    ]
)
@app.callback(
    Output(component_id='out-div', component_property='children'),
    [Input(component_id='inp', component_property='value')])

    #Output("map", "figure"),
    #[Input("value-selected", "value")]

def update_output_div(input_value):
    return 'Test field :"'.format(input_value)

#def update_figure(selected):
#    return "Temp"

if __name__ == '__main__':
    app.run_server()
