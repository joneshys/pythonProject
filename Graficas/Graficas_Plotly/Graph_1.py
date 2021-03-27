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

# Trae los 5 primeros registros
# print(df[:5])

# Obtiene la 5 primeras filas y con la ubicacióin de las columnas[2,3,5,10] del CSV
# print(df.iloc[:5, [2,3,5,10]])

# Obtiene la 5 primeras filas y con los nombres de las columbas ['Platform','Genre'] del CSV
# print(df.loc[:5, ['Platform','Genre']])

# Obtener las categorias o nombres de las columnas
# print(df.Genre.nunique()) # Cantidad de categorias
# print(df.Genre.unique()) # Lista de las categorias

# Obtener fechas por orden
#print(sorted(df.Year.unique())) # Obtiene una lista de los años del csv

# Data visualización with plotly
#------------------------------------------------

# creación de una torta
# name es nombre de la categoria, y values me trea el valor de la categoria
# fig_pie = px.pie(data_frame=df, names='Genre', values='Japan Sales')
# fig_pie.show()

# creación de barra
#fig_bar = px.bar(data_frame=df, x='Genre', y='Japan Sales')
#fig_bar.show()

# creación de barra
# si en x hay categorias y y valores obtengo barras de los valores de las categorias
#fig_hist = px.histogram(data_frame=df, x='Genre', y='Japan Sales')
#fig_hist.show()

# creación de barra
# si en x hay años y valores obtengo el histograma de los valores de las categorias
#fig_hist = px.histogram(data_frame=df, x='Year', y='Japan Sales')
#fig_hist.show()


# Data interantivo grahp with Dash
#------------------------------------------------

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