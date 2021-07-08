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
color1 = "#00BF16"
color2 = "#00BF16"


def create_privacy_statistic():
    confident =0
    not_confident =0
    
    

    for index, row in df.iterrows():
        if(row['PRIVACYNEWS1_W49'] == 1 or row['PRIVACYNEWS1_W49'] == 2):
            confident +=1
        elif(row['PRIVACYNEWS1_W49'] == 3 or row['PRIVACYNEWS1_W49'] == 4):
            not_confident +=1

    final_confident = (confident / (confident+not_confident))*100
    if(final_confident > 50):
        color1 = "#BF0400"
    
    stat = "{} % of Americans do not closely follow news about privacy issues.".format(round(final_confident,1))

    return html.H4(stat,style={"text-align": "center","background": color1,"color": "#ffffff"})


def create_understand_statistic():
    confident =0
    not_confident =0
    
    

    for index, row in df.iterrows():
        if(row['UNDERSTANDCO_W49'] == 1 or row['UNDERSTANDCO_W49'] == 2):
            confident +=1
        elif(row['UNDERSTANDCO_W49'] == 3 or row['UNDERSTANDCO_W49'] == 4):
            not_confident +=1

    final_confident = (confident / (confident+not_confident))*100

    if(final_confident < 50):
        color2 = "#BF0400"

    stat = "{} % of Americans feel they understand what companies do with the data they collect on them.".format(round(final_confident,1))

    return html.H4(stat,style={"text-align": "center","background": color2,"color": "#ffffff"})


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

    return px.pie(df2,values = 'Americans', names = 'Feeling')



def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [

                    html.Div(
                            [
                                html.H5("Use Case"),
                                html.Br([]),
                                html.P(
                                    "\
                                    Signal is an end to end encrypted messaging app. \
                                    It is open source and focuses on how safe, secure, and private the messaging is. \
                                    The signal advertisment team can use this  \
                                    dashboard to get better information on how much people know about internet security and privacy. \
                                    This allows them to better tailor their advertisements to show that signal is a better app than What's App.\
                                    Each section of the dashboard is made to give clear information without distracting the user.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                            ],
                                className="product",
                    ),

                    html.Div(
                            [
                                html.H5("Dataset"),
                                html.Br([]),
                                html.P(
                                    "\
                                    The dataset was taken from pewresearch.org \"American Trends Panel Wave 49\"\
                                    which was a survey that focused on what Americans know about internet security\
                                    and how they feel about data privacy. It was conducted in 2019.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                            ],
                                className="product",
                    ),
                    
                    html.Div([
                        html.Br([]),
                        html.H2("How much of their online activity do Americans believe is being tracked by advertisers and tech companies?"),
                        dcc.Graph(figure=create_tracking_graph(), config= {'displaylogo': False}) # add ID like id='the_graph'for css
                    ]),
                    html.Div([
                        create_privacy_statistic()
                    ]),
                    html.Div([
                        create_understand_statistic()
                    ]),
                    
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )