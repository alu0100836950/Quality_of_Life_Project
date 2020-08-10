import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

import plotly.figure_factory as ff
import plotly.graph_objs as go

#Read dataset
df = pd.read_csv("Indices.csv")

#List of dataset column
available_indicators = list(df)


app = dash.Dash()

app.layout = html.Div(children = [

    #histograma
    html.H1(children = 'Comparación entre los valores calidad de vida de Numbeo y una encuesta de Europa'),
        html.H3('El objetivo de trabajo es realizar las comparaciones entre la forma de medir la calidad de vida, estos es, hacerlas de forma cualitativa(encuesta de europa) o de forma cuantitativa(Formula de numbeo)'),
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
            html.Div(id='histogram_graph')
        ]),
        
])

#callback for Histogram
@app.callback(
    dash.dependencies.Output(component_id='histogram_graph', component_property='children'),
    [dash.dependencies.Input('histogram_xaxis-column', 'value'),
        dash.dependencies.Input('histogram_xaxis-column2','value'),
        dash.dependencies.Input('histogram_yaxis-column', 'value')
    ])    
def update_value(xaxis_column_name, xaxis_column_name2, yaxis_column_name):


    x= df[yaxis_column_name]
    #print(x)
    return dcc.Graph(
        id='histogram_graph',
        figure={
            'data': [
                
                {'x': x, 'y': df[xaxis_column_name], 'type': 'line', 'name': 'Value_Numbeo'},
                {'x': x, 'y': df[xaxis_column_name2], 'type': 'line', 'name': u'Value_Europa'},
            ],
            'layout': go.Layout(
            
                xaxis=dict(
                    title=yaxis_column_name
                ),
                yaxis=dict(
                    title='Position of Ranking'
                ),

            )
        }
    )



if __name__ == '__main__':
    app.run_server(debug=True)
