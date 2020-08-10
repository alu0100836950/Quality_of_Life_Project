import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()


app.layout = html.Div([
    dcc.Input(id='input', value='Escribe algo aqui!', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_value(input_data):
    return ' Input: "{}"'.format(input_data)


# app.layout = html.Div(children=[
#     html.H1(children='Empezando con dash'),
#     dcc.Graph(
#         id='ejemplo',
#         figure={
#             'data':[
#             {'x': [1, 2, 3, 4], 'y': [1, 8, 3, 7], 'type': 'line', 'name': 'Bicicletas'},
#             {'x': [1, 2, 3, 4], 'y': [5, 2, 8, 8], 'type': 'bar', 'name': 'Bicicletas electricas'},
#             ],
#             'layout': {
#                 'title': 'Ejemplo basico en Dash'
#             }
#         }
#     )
# ])



if __name__ == '__main__':
    app.run_server(debug=True)
