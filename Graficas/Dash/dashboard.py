import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table

from dash.dependencies import Input, Output, State
from pull_news import get_news
from dash.exceptions import PreventUpdate

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id="query_String",
        placeholder="Please choose a criteria",
        type="text"
    ),
    html.Button('Buscar', id="button_buscar"),
    html.Div(id="content")
])

@app.callback(Output("content", "children"),
              [Input("button_buscar", "n_clicks")],
              [State("query_String", "value")])

def get_news_callback(v, q):
    print(v)
    if v!= None:
        news = get_news(q)
    else:
        raise PreventUpdate
    html_string = []
    for n in news:
        html_string.append(
            html.Div([
                html.H1([n[0]], className="title"),
                html.P(n[1], className="p"),
                html.P(n[2])
            ])
        )

    return html_string

app.run_server(debug=True)