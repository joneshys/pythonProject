import dash
import plotly.express as px
import pandas as pd
import csv
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

# Data exploration with pandas
#------------------------------------------------
df = pd.read_csv('AMI_Instances.csv')
print(df[:5])
print(df.Componente.nunique()) # Cantidad de categorias
print(df.Componente.unique()) # Lista de las categorias
