import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

import plotly.figure_factory as ff
import plotly.graph_objs as go

#Read dataset
df = pd.read_csv("Numbeo_2015.csv")

#List of dataset column
available_indicators = list(df)


app = dash.Dash()

app.layout = html.Div(children = [

    #histograma
    html.H1(children = 'Histograma de Numbeo 2015'),
        html.Div([
            html.Div([
                #filter by column
                dcc.Dropdown(
                    id='histogram_xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value = available_indicators[2]
                ),

                #filter choise
                dcc.RadioItems(
                    id='histogram_xaxis-type',
                    options=[{'label':i,'value':i} for i in ['Filter', 'No Filter']],
                    value='No filter',
                    labelStyle = {'display': 'inline-block'}
                ),
                #filter by column
                dcc.Dropdown(
                    id='histogram_xaxis-column2',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value = available_indicators[2]
                ),
            ],
            style= {'width': '100%', 'display': 'inline-block'}),

            html.Div( [
                #y axis data selection
                dcc.Dropdown(
                    id='histogram_yaxis-column',
                    options=[{'label':i, 'value': i} for i in available_indicators],
                    value=available_indicators[1]
                )
            ],
            style={'width':'100%', 'float': 'center', 'vertical-align': 'top', 'display' :'inline-block'}),
        
        ]),
        
        #plot graph
        dcc.Graph(id='histogram_graph')], style={'width':'100%', 'float': 'center', 'vertical-align': 'top', 'display' :'inline-block'})


#callback for Histogram
@app.callback(
    dash.dependencies.Output('histogram_graph', 'figure'),
    [dash.dependencies.Input('histogram_xaxis-column', 'value'),
        dash.dependencies.Input('histogram_xaxis-column','value'),
        dash.dependencies.Input('histogram_yaxis-column', 'value'),
        dash.dependencies.Input('histogram_xaxis-type', 'value')
    ])
def update_value(xaxis_column_name, xaxis_column_name2, yaxis_column_name, xaxis_type):
    # if xaxis_type == 'Filter':
    #     data = []
    #     data2 = []
    #     for value in df[yaxis_column_name].unique():

    #         trace = go.Line(
    #             #x=df[yaxis_column_name].values,
    #             y=df[xaxis_column_name].values,
    #             x=df[df[yaxis_column_name] == value][xaxis_column_name].values,
    #             name=str(value),
    #         )
    #         data.append(trace)
    # else:
    #     trace = go.Line(
    #         x=df[yaxis_column_name].values,
    #         y=df[xaxis_column_name].values,
    #     )
    #     trace2 = go.Line(
    #         x=df[yaxis_column_name].values,
    #         y=df[xaxis_column_name2].values,
    #     )
    #     data= [trace]
    #     data2 = [trace2]

 
    # return {

    #     "data": data,
    #     "data": data2,
    #     "layout": go.Layout(
    #         barmode='group',
    #         xaxis=dict(
    #             title=yaxis_column_name
    #         ),
    #         yaxis=dict(
    #             title='count'
    #         ),
    #     )
    # }
    return dcc.Graph(
        id='histogram_graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
            }
        }
    )



if __name__ == '__main__':
    app.run_server(debug=True)
