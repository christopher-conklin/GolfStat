import dash_core_components as dcc
import dash_html_components as html
import dash_table

scorecard = dash_table.DataTable(id='scorecard',
                                 columns=[{'name':'Hole', 'id': 'labels'}] +
                                         [{'name': f'{i+1}', 'id': f'hole{i+1}'} for i in range(18)],
                                 data=[{'labels': 'Yardage'},
                                       {'labels': 'Par'},
                                       {'labels': 'Score'}],
                                 editable=True)

new_course_layout = html.Div([
    html.Label('Course Name'),
    dcc.Input(id='edit-course-name'),
    html.Label('Course Location (optional)'),
    dcc.Input(id='edit-course-location')
])

choose_tee_div = html.Div([
                        html.Label('Choose Tee'),
                        dcc.Dropdown(
                            options=[{'value': 'new-tee', 'label': 'New Tee...'}],
                            id='choose-tee',
                        )])

new_tee_div = html.Div([
    html.Label('Tee Name'),
    dcc.Input(id='tee-name'),
    dash_table.DataTable(id='new-tee-holes',
                         columns=[{'name':'Hole', 'id': 'labels', 'editable': False}] +
                                 [{'name': f'{i+1}', 'id': f'hole{i+1}'} for i in range(18)],
                         data=[{'labels': 'Yardage'},
                               {'labels': 'Par'}
                               ],
                         editable=True,
                         style_header={'textAlign': 'center'}),
    html.Button('Submit', id='submit-button')
])

new_round_div = html.Div([
    html.Label('Choose Course'),
    dcc.Dropdown(
        options=[
            {'value': 'new-course', 'label': 'New Course...'}
        ],
        id='choose-course'
    ),
    html.Div(id='new-course-div'),
    html.Div(id='tee-div'),
    html.Div(id='hole-entry')
])
