#Importing libraries
import pandas as pd
import numpy as np
import glob
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


#Read csv file
df=pd.read_excel(r'C:\Users\saurabh_kulkarni\Desktop\Litepoint DRT.xlsx',sheet_name='Yield')


###############################################################################
# DASHBOARD USING DASH
###############################################################################

#Define CSS style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Define colors dictionary for background and text colors
colors = {
    'background': '#111111',
    'text': '#000080'
}

#Define app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Markdown text for Volume charts
markdown_text='''
### Volume by Products
'''

#Layout of app
app.layout=html.Div(children=[
        html.H1(children='Process & Yield Dashboard', style={'textAlign':'center','color':colors['text']}),

        #Yield chart using scatter, Yield by process chart
        dcc.Graph(
                id='yield_by_process',
                figure_yield={
                        'data':[{'type':'scatter','mode':'lines+markers+text','x':df.Process,'y':df.Yield,'text':df.Yield,'textposition':'bottom center','textfont':{'color':colors['text']}}],
                        'layout':{
                                'yaxis':{
                                        'range':[0,100]
                                        },
                                'title':{
                                        'text':'Yield by Process',
                                        'font':{
                                                'color':colors['text']
                                                }
                                        }
                                }
                        }
                ),
        #Volume by process bar chart
        dcc.Graph(
                id='volume_by_process',
                figure_volume={
                        'data':[{'type':'bar','x':df.Process,'y':df.Tested,'text':df.Tested,'textposition':'auto','textfont':{'color':colors['text']}}],
                        'layout':{
                                'title':{
                                        'text':'Volume by Process',
                                        'font':{
                                                'color':colors['text']
                                                }
                                        }
                                }
                        }
                ),

        dcc.Markdown(children=markdown_text,style={'textAlign':'center','color':colors['text']})
        ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
