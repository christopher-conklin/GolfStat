import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from web.round_course_layout import new_round_div
import web.round_course_callbacks as rc_callbacks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title = 'GolfStat'

app.layout = html.Div(children=[
    html.Div(children='Please ensure you are using a Chrome browser'),
    dcc.Tabs(id='tabs', value='new-round', children=[
        dcc.Tab(label='New Round', value='new-round'),
        dcc.Tab(label='Statistics', value='statistics')
    ]),
    html.Div(id='tabs-content')

])

rc_callbacks.register_callbacks(app)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'new-round':
        return new_round_div
    if tab == 'stats-tab':
        pass



if __name__ == '__main__':
    app.run_server(debug=True)