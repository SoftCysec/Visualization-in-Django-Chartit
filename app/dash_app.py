import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

@app.callback(
    Output(component_id='bar-chart', component_property='figure'),
    Input(component_id='upload-data', component_property='contents')
)
def update_bar_chart(contents):
    if contents is None:
        return {}
    else:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        fig = px.bar(df, x='x', y='y')
        return fig

@app.callback(
    Output(component_id='line-chart', component_property='figure'),
    Input(component_id='upload-data', component_property='contents')
)
def update_line_chart(contents):
    if contents is None:
        return {}
    else:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        fig = px.line(df, x='x', y='y')
        return fig


app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),

    html.Div([
        html.Div([
            dcc.Graph(
                id='bar-chart'
            )
        ], className="six columns"),

        html.Div([
            dcc.Graph(
                id='line-chart'
            )
        ], className="six columns"),

    ], className="row")
])


if __name__ == '__main__':
    app.run_server(debug=True)
