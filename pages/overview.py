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



def create_privacy_statistic():
    confident =0
    not_confident =0
    
    

    for index, row in df.iterrows():
        if(row['PRIVACYNEWS1_W49'] == 1 or row['PRIVACYNEWS1_W49'] == 2):
            confident +=1
        elif(row['PRIVACYNEWS1_W49'] == 3 or row['PRIVACYNEWS1_W49'] == 4):
            not_confident +=1

    final_confident = (confident / (confident+not_confident))*100

    return "{} % of Americans do not closely follow news about privacy issues.".format(round(final_confident,1))


def create_understand_statistic():
    confident =0
    not_confident =0
    
    

    for index, row in df.iterrows():
        if(row['UNDERSTANDCO_W49'] == 1 or row['UNDERSTANDCO_W49'] == 2):
            confident +=1
        elif(row['UNDERSTANDCO_W49'] == 3 or row['UNDERSTANDCO_W49'] == 4):
            not_confident +=1

    final_confident = (confident / (confident+not_confident))*100

    return "{} % of Americans feel they understand what companies do with the data they collect on them.".format(round(final_confident,1))

def create_tracking_graph():

    one =0
    two =0
    three =0
    four =0
    five =0

    for index, row in df.iterrows():
        if(row['TRACKCO1a_W49'] == 1):
            one +=1
        elif(row['TRACKCO1a_W49'] == 2):
            two +=1
        elif(row['TRACKCO1a_W49'] == 3):
            three +=1
        elif(row['TRACKCO1a_W49'] == 4):
            four +=1
        elif(row['TRACKCO1a_W49'] == 5):
            five +=1
    
    data = [['All or Almost all',one ],['Most of it',two ],['Some of it',three ],['Very little of it', four],['None of it',five]]

    df2 = pd.DataFrame(data, columns=['Feeling', 'Americans'])

    return px.pie(df2,values = 'Americans', names = 'Feeling', title = 'How much of what you do online is being tracked by advertisers and tech companies')



def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [
                    
                    html.Div([
                        dcc.Graph(figure=create_tracking_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                    html.Div([
                        html.H4(create_privacy_statistic())
                    ]),
                    html.Div([
                        html.H4(create_understand_statistic())
                    ]),
                    
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )