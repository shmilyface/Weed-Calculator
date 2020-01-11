# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ##  DISCLAIMER
            This calculator is meant for educational purposes only.


            These statements have not been evaluated by the Food Drug Administration.


            This service is not intended to replace a medical professional.


            We are not medical professionals.


            **Use at your own risk.**

            
            **For more information on responsible dosing:**
            
            https://www.consumeresponsibly.org/limit/

            """
        ),
        dcc.Link(dbc.Button('I am 18 or Older', color='primary'), href='/potency-calculator')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/add-weed-tFkScFEdh7c-unsplash.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])
