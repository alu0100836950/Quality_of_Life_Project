import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

import pandas as pd

import plotly.figure_factory as ff
import plotly.graph_objs as go

#Read dataset
#df = pd.read_csv("Indices.csv")

#List of dataset column
#available_indicators = list(df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = []

app.layout = html.Div(children = [
    html.H1(children = 'Quality of Life in Europe Cities'),
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
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    
    
    #Graph
        html.Div([
            html.Div([
                #filter by column
                
                dcc.Dropdown(
                    id='histogram_xaxis-column',
                    options=[{'label': i, 'value': i} for i in ['Indice_Numbeo']],
                    value = 'Indice_Numbeo'
                ),

                #filter choise
                
                dcc.Dropdown(
                    id='histogram_xaxis-column2',
                    options=[{'label': i, 'value': i} for i in ['Indice_Europa']],
                    value = 'Indice_Europa'
                ),
            ],
            style= {'width': '100%', 'display': 'inline-block'}),

            html.Div( [
                #y axis data selection
                
                dcc.Dropdown(
                    id='histogram_yaxis-column',
                    options=[{'label':i, 'value': i} for i in ['Ciudad']],
                    value='Ciudad'
                )
            ],
            style={'width':'100%', 'float': 'center', 'vertical-align': 'top', 'display' :'inline-block'}),
            html.Div(id='histogram_graph'),
           
    ]),
    
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
            
        ),
        dcc.Graph(
            id='histogram_graph',
            figure={
                'data': [
                    
                    {'x': df['Ciudad'], 'y': df['Indice_Numbeo'], 'type': 'line', 'name': 'Value_Numbeo'},
                    {'x': df['Ciudad'], 'y': df['Indice_Europa'], 'type': 'line', 'name': u'Value_Europa'},
                ],
                'layout': go.Layout(
                
                    xaxis=dict(
                        title='Ciudad'
                    ),
                    yaxis=dict(
                        title='Position of Ranking'
                    ),

                )
            }
        )

    ])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children






#callback for Graph
# @app.callback(
#     dash.dependencies.Output(component_id='histogram_graph', component_property='children'),
#     [dash.dependencies.Input('histogram_xaxis-column', 'value'),
#         dash.dependencies.Input('histogram_xaxis-column2','value'),
#         dash.dependencies.Input('histogram_yaxis-column', 'value')
#     ])    
# def update_value(xaxis_column_name, xaxis_column_name2, yaxis_column_name):


    # x= df[yaxis_column_name]
    # #print(x)
    # return dcc.Graph(
    #     id='histogram_graph',
    #     figure={
    #         'data': [
                
    #             {'x': x, 'y': df[xaxis_column_name], 'type': 'line', 'name': 'Value_Numbeo'},
    #             {'x': x, 'y': df[xaxis_column_name2], 'type': 'line', 'name': u'Value_Europa'},
    #         ],
    #         'layout': go.Layout(
            
    #             xaxis=dict(
    #                 title=yaxis_column_name
    #             ),
    #             yaxis=dict(
    #                 title='Position of Ranking'
    #             ),

    #         )
    #     }
    # )



if __name__ == '__main__':
    app.run_server(debug=True)
