import dash_core_components as dcc
import dash_html_components as html
#import plotly.graph_objs as go
import plotly.express as px

from utils import Header, make_dash_table

import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = pd.read_csv(DATA_PATH.joinpath('master.csv'))

def create_questionnaire_graph():
    data = [calc_question(1,4),calc_question(2,2),calc_question(3,1),calc_question(4,1),calc_question(5,5),calc_question(6,3),calc_question(7,1),calc_question(8,3),calc_question(9,1)]


    group_labels = label_helper(9)

    df2 = pd.DataFrame(data,index=group_labels)
    df2.columns = ['Right','Wrong']
    df2.index.names = ['Question #']
    #might need to make a drop down to choose between each question to simplify all this
    return px.bar(df2, barmode='group',title = 'Right vs Wrong Answers', orientation='h',labels={"value": "Submissions","variable":" "})

def create_questionnaire_table():
    options=[
            {'label': 'Question 1', 'value': 'What is a website cookie?'},
            {'label': 'Question 2', 'value': 'Which is the largest source of revenue for social media companies?'},
            {'label': 'Question 3', 'value': 'What is a privacy policy?'},
            {'label': 'Question 4', 'value': 'What does the s in HTTPS mean?'},
            {'label': 'Question 5', 'value': 'Where will you encounter a phishing attempt'},
            {'label': 'Question 6', 'value': 'Which two companies belong to facebook'},
            {'label': 'Question 7', 'value': 'What is net neutrality'},
            {'label': 'Question 8', 'value': 'What does private browsing in a web browser do?'},
            {'label': 'Question 9', 'value': 'What is two-factor authentication?'},
            ]

    options.reverse()

    df2 = pd.DataFrame(options)

    return make_dash_table(df2)

def label_helper(amount):
    labels = []

    for x in range(1,amount+1):
        labels.append('question {}'.format(x))

    return labels


def calc_question(question, answer):

    column_name = 'KNOW{}_W49'.format(question)
    right =0
    wrong =0

    for index, row in df.iterrows():
        if(row[column_name] == answer):
            right +=1
        else:
            wrong +=1
    
    #data =[['right',right],['wrong',wrong]]
    data = [right,wrong]

    return data




def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [
                    html.H5("Basic Internet Privacy and Security Knowledge"),
                    html.Div([
                        dcc.Graph(figure=create_questionnaire_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                    html.Div([
                        html.Table(create_questionnaire_table())
                    ]),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )