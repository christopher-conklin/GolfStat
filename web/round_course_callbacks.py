from dash.dependencies import Input, Output, State
from web.round_course_layout import *


def register_callbacks(app):
    @app.callback(
        [Output('new-course-div', 'children'), Output('tee-div', 'children')],
        [Input('choose-course', 'value')]
    )
    def set_course(course_selection):
        if course_selection == 'new-course':
            return new_course_layout, new_tee_div
        elif course_selection is None:
            return None, None
        else:
            return None, choose_tee_div

    # @app.callback(Output('hole-entry', 'children'),
    #               [ Input('tee-div', 'children')],
    #               [State('choose-course', 'value')]
    #               )
    # def set_hole_entry(tee_div, course_choice):
    #     if tee_div is None and course_choice is 'new-course':
    #         return new_tee_div
    #     else:
    #         return None
