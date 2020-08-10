import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

import plotly.graph_objs as go
import io
import base64


app = dash.Dash()

colors = {
"graphBackground": "#F5F5F5",
"background": "#ffffff",
"text": "#000000"
}

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.A('Seleccione un archivo csv')
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
    dcc.Graph(id='Mygraph'),
    html.Div(id='output-data-upload')
])


# def parse_data(contents, filename):
#     content_type, content_string = contents.split(',')
    
#     decoded = base64.b64decode(content_string)

#     try:
#         if 'csv' in filename:
#             # Assume that the user uploaded a CSV or TXT file
#             df = pd.read_csv(
#                 io.StringIO(decoded.decode('utf-8')))
#     except Exception as e:
#         print(e)
#         return html.Div([
#             'There was an error processing this file.'
#         ])

#     return df


@app.callback(Output('Mygraph', 'figure'),
    [
        Input('upload-data', 'contents'),
        Input('upload-data', 'filename')
    ])

def update_graph(contents, filename):

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    print(filename)
    df = pd.read_csv('Numbeo_2015.csv')

    x = []
    y = []
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = df.set_index(df.columns[0])
        print(df)
        x = df['Ciudad']
        y = df['value']
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                mode='lines+markers'
            )
        ],
        layout = go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"]
        )
    )
        
    return fig

# @app.callback(Output('output-data-upload', 'children'),[
#     Input('upload-data', 'contents'),
#     Input('upload-data', 'filename')
# ])
# def update_table(contents, filename):
#     table = html.Div()

#     if contents:
#         contents = contents[0]
#         filename = filename[0]
#         df = parse_data(contents, filename)

#         table = html.Div([
#             html.H5(filename),
#             dash_table.DataTable(
#                 data=df.to_dict('rows'),
#                 columns=[{'name': i, 'id': i} for i in df.columns]
#             ),
#             html.Hr(),
#             html.Div('Raw content'),
#             html.Pre(contents[0:200] + '...', style={
#                 'whiteSpace': 'pre-wrap',
#                 'wordBreak': 'break-all'
#             })
#         ])
#     return table


if __name__ == '__main__':
    app.run_server(debug=True)