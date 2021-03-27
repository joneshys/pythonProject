import dash
import plotly.express as px
import pandas as pd
import csv
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

# Data exploration with pandas
#------------------------------------------------
df = pd.read_csv('vgsales.csv')

app = dash.Dash(__name__)
app.layout=html.Div([
    html.H1("List Drop Example"),
    dcc.Dropdown(id='Genre-Choice', options=[{'label':x, 'value':x}
                                             for x in sorted(df.Genre.unique())],
                 value='Sports'),
    dcc.Graph(id='my_grahp', figure= {})
], style={'marginLeft': 'auto', 'marginRight': 'auto', 'textAlign': 'center',})

@app.callback(
    Output(component_id='my_grahp', component_property='figure'),
    Input(component_id='Genre-Choice', component_property='value')
)

def interactive_grahp(value_genre):
    print(value_genre)
    dff = df[df.Genre==value_genre]
    fig = px.bar(data_frame=dff, x='Year', y='Japan Sales')
    return fig

if __name__=='__main__':
    app.run_server(host="0.0.0.0",port=5000, debug=True)