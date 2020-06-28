from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import requests
from web.round_course_layout import *


def register_callbacks(app):
    # @app.callback(
    #     [Output('new-course-div', 'children'), Output('tee-div', 'children')],
    #     [Input('choose-course', 'value')]
    # )
    # def set_course(course_selection):
    #     if course_selection == 'new-course':
    #         return new_course_layout, new_tee_div
    #     elif course_selection is None:
    #         return None, None
    #     else:
    #         return None, choose_tee_div

    # @app.callback(Output('hole-entry', 'children'),
    #               [ Input('tee-div', 'children')],
    #               [State('choose-course', 'value')]
    #               )
    # def set_hole_entry(tee_div, course_choice):
    #     if tee_div is None and course_choice is 'new-course':
    #         return new_tee_div
    #     else:
    #         return None

    @app.callback(
        Output('choose-course', 'options'),
        [Input('choose-course', 'search_value')]
    )
    def get_courses(search_term):
        if not search_term:
            raise PreventUpdate
        auth_header = {'Authorization':
                           'Bearer eyJhbGciOiJIUzI1NiJ9.eyJnaGluX251bWJlciI6IjU0NDE3ODkiLCJzdWIiOiIyIiwic2NwIjoidXNlci'
                           'IsImF1ZCI6bnVsbCwiaWF0IjoxNTkzMjc1NzI2LCJleHAiOjE1OTMzMTg5MjYsImp0aSI6IjMyNWExNDBmLWZiNjIt'
                           'NGM1Yy1hMGZhLTdhMzYxNDI5NmIwMSJ9.Xa2H-zsw9ADXHWjym5t51adtLRQdQf9ymk1nK4x1ZH8'}
        course_list = requests.get(f'https://api2.ghin.com/api/v1/crsCourseMethods.asmx/SearchCourses.json?'
                                   f'name={search_term}',
                                   headers=auth_header).json()['courses']
        display_list = [{'label': f'{cl["CourseName"]}; {cl["City"]}, {cl["State"] if cl["State"] else ""}', 'value': str(cl['CourseID'])} for cl in course_list]
        if len(display_list) > 20:
            return display_list[:20]
        else:
            return display_list

