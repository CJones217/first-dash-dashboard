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

def create_secur_graph():

    one =0
    two =0
    three =0 

    for index, row in df.iterrows():
        if(row['SECUR1_W49'] == 1):
            one +=1
        elif(row['SECUR1_W49'] == 2):
            two +=1
        elif(row['SECUR1_W49'] == 3):
            three +=1
    
    data = [['More Secure',one ],['Less Secure',two ],['About the Same',three ]]

    df2 = pd.DataFrame(data, columns=['Feeling', 'Percent of Americans'])

    return px.pie(df2,values = 'Percent of Americans', names = 'Feeling', title = 'How Americans feel about personal information security compared to 5 years ago')

def create_privacyreg_graph():

    one =0
    two =0
    three =0
    four =0

    for index, row in df.iterrows():
        if(row['PRIVACYREG_W49'] == 1):
            one +=1
        elif(row['PRIVACYREG_W49'] == 2):
            two +=1
        elif(row['PRIVACYREG_W49'] == 3):
            three +=1
        elif(row['PRIVACYREG_W49'] == 4):
            four +=1
    
    data = [['A Great Deal',one ],['Some',two ],['Very Little',three ],['Not at all', four]]

    df2 = pd.DataFrame(data, columns=['Feeling', 'Americans'])

    return px.pie(df2,values = 'Americans', names = 'Feeling', title = 'Americans Knowledge of data privacy laws')

def create_pwman_graph():
    one =0
    two=0

    for index, row in df.iterrows():
        if(row['PWMAN_W49']==1):
            one+=1
        elif(row['PWMAN_W49']==2):
            two+=1
    
    data = [['yes',one],['no',two]]

    df2 = pd.DataFrame(data, columns=['Answer','Americans'])

    return px.pie(df2,values = 'Americans', names='Answer', title = 'Password manager use by Americans')



def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [
                    html.H5("Americans Understanding of Security"),
                    html.Div([
                        dcc.Graph(figure=create_secur_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                    html.Div([
                        dcc.Graph(figure=create_privacyreg_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                    html.Div([
                        dcc.Graph(figure=create_pwman_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )