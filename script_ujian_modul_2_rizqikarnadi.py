import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import dash_table
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

tsaclaims = pd.read_csv('tsa_claims_ujian.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe, max_rows=10) :
    return html.Table(
        
    
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        [html.Tr([
            html.Td(str(dataframe.iloc[i,col])) for col in range(len(dataframe.columns))
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app.title = 'Dashboard TSA Claims'

app.layout = html.Div([
    html.H1('Dashboard TSA Claims'),

    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data TSA Claims', value='tab-1', children=[
            html.Div([
                html.Div([
                    
                )
                ]
            ]
        ])
    
                