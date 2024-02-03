#!/usr/bin/env python
# coding: utf-8

# # IBM Capstone project
# ## Plotly data visualization code

# In[63]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

data = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)
max_payload = data['Payload Mass (kg)'].max()
min_payload = data['Payload Mass (kg)'].min()

def draw_rate_of_success(filtered, launch_site):
    fig = px.pie(filtered, values='class', 
                names=['Succeeded', 'Failed'], 
                title=f'Succes Rate of "{launch_site}" SpaceX launch site')
    return fig

app = dash.Dash(__name__)

app.layout = html.Div([html.H1("SpaceX Launch Records Dashboard", 
                               style={'textAlign': 'center', 'color': '#503D36',
                                      'font-size': 40}),
                       dcc.Dropdown(id="site-dropdown",
                                    options=[{'label': 'All Sites', 'value': 'ALL'},
                                             {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                             {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                             {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                             {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                    value='ALL',
                                    placeholder="Select Launch Sites"),
                       html.Div(dcc.Graph(id='success-pie-chart')),
                       html.Br(),
                       html.Div(dcc.RangeSlider(id='payload-slider', min=0, max=10000, 
                                                step=1000, marks={0: '0', 100: '100'}, 
                                                value=[min_payload, max_payload]),
                               ),
                       html.Div(dcc.Graph(id='success-payload-scatter-chart')),          
])

# Function decorator to specify function input and output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'CCAFS SLC-40':
        filtered = data[data["Launch Site"] == "CCAFS SLC-40"]["class"].value_counts().rename('class')
        fig = draw_rate_of_success(filtered, entered_site)
        
    elif entered_site == 'CCAFS LC-40':
        filtered = data[data["Launch Site"] == "CCAFS LC-40"]["class"].value_counts().rename('class')
        fig = draw_rate_of_success(filtered, entered_site)
        
    elif entered_site == 'VAFB SLC-4E':
        filtered = data[data["Launch Site"] == "VAFB SLC-4E"]["class"].value_counts().rename('class')
        fig = draw_rate_of_success(filtered, entered_site)
        
    elif entered_site == 'KSC LC-39A':
        filtered = data[data["Launch Site"] == "KSC LC-39A"]["class"].value_counts().rename('class')
        fig = draw_rate_of_success(filtered, entered_site)

    else:
        filtered = data['Launch Site'].value_counts()
        fig = px.pie(filtered, values='Launch Site', 
                    names=filtered.index, 
                    title='Flight distribution of SpaceX launch sites')
        # return the outcomes piechart for a selected site
    
    return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'), 
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_plot(site, payload):
    if site == "CCAFS SLC-40":
        filter = data[data["Launch Site"]=="CCAFS SLC-40"]
        fig = px.scatter(data_frame=filter, x="Payload Mass (kg)", y="class", color="Booster Version")
        
    elif site == "CCAFS LC-40":
        filter = data[data["Launch Site"]=="CCAFS LC-40"]
        fig = px.scatter(data_frame=filter, x="Payload Mass (kg)", y="class", color="Booster Version")
        
    elif site == "CCAFS LC-40":
        filter = data[data["Launch Site"]=="CCAFS LC-40"]
        fig = px.scatter(data_frame=filter, x="Payload Mass (kg)", y="class", color="Booster Version")
       
    else:
        fig = px.scatter(data_frame=data, x="Payload Mass (kg)", y="class", color="Booster Version")
        
    return fig 

# Run the application
if __name__ == '__main__':
    app.run_server()


# In[ ]:




