#Importing libraries
import pandas as pd
import numpy as np
import glob
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


#Read csv file
df=pd.read_excel(r'C:\Users\saurabh_kulkarni\Desktop\Litepoint DRT.xlsx',sheet_name='Yield')


###############################################################################
# DASHBOARD USING DASH
###############################################################################

#Define CSS style
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Define app
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app=dash.Dash()

#Define colors 
colors = {
    'background': '#ffffff',
    'text': '#000080'
}

#Define how the dashboard will look like


###Older code
'''
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Litepoint Process & Quality Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='yield_by_process',
        figure={
            'data': [
                {'x':df['Process'],'y':df.Yield,'type':'line','name':'Yield'}
            ],
            'layout': {
                'title':{"text":'Yield by Process'},
                'yaxis_title':{"text":"Process"},
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])
'''

app.layout=html.Div([
        dcc.Graph(
                id='yield_by_process',
                figure= go.Figure([go.Bar(x=df['Process'],y=df['Yield'])])                                
                )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)