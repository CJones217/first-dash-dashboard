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



def create_fb_and_concern():
    
    use_fb =0
    use_fb_concern =0
    use_fb_no_concern =0
    no_fb =0
    no_fb_no_concern =0
    no_fb_concern =0
    dump1=0
    dump2=0

    for index, row in df.iterrows():
        if(row['SOCMEDIAUSEa_W49'] == 1):
            use_fb +=1
            if(row['CONCERNCO_W49'] == 1 or row['CONCERNCO_W49'] == 2):
                use_fb_concern +=1
            elif(row['CONCERNCO_W49'] == 3 or row['CONCERNCO_W49'] == 4):
                use_fb_no_concern +=1
            else:
                dump1+=1
                use_fb-=1
            

        elif(row['SOCMEDIAUSEa_W49'] == 2):
            no_fb +=1
            if(row['CONCERNCO_W49'] == 1 or row['CONCERNCO_W49'] == 2):
                no_fb_concern +=1
            elif(row['CONCERNCO_W49'] == 3 or row['CONCERNCO_W49'] == 4):
                no_fb_no_concern +=1
            else:
                dump2+=1
                no_fb-=1

    return [use_fb,use_fb_concern,use_fb_no_concern,no_fb,no_fb_concern,no_fb_no_concern,dump1,dump2]


def create_fb_only_graph():

    pulldata = create_fb_and_concern()
    data = [pulldata[0]+pulldata[6],pulldata[3]+pulldata[7]]


    df2 =pd.DataFrame(data, index = ['Use Facebook','No Facebook Use'])
    #df2.columns['use facebook','no facebook use']
    df2.index.names = [' ']

    graph = px.bar(df2,title = 'How Many People Use Facebook',labels={"value": "Submissions","variable":" ti"})
    graph.layout.update(showlegend=False)
    graph.update_traces( hovertemplate=None)

    return graph

def create_fb_and_concern_graph():

    pulldata = create_fb_and_concern()
    data = [[pulldata[0],pulldata[1],pulldata[2]],[pulldata[3],pulldata[4],pulldata[5]]]

    df2 = pd.DataFrame(data,index = ['Use Facebook','No Facebook Use'])
    df2.columns = ['Facebook','Concern','No Concern']
    df2.index.names = [' ']

    graph = px.bar(df2, barmode='group',title = 'Facebook Users And Their Concern For Their Private Data Usage',labels={"value": "Submissions","variable":" "})
    graph.update_traces( hovertemplate=None)

    return graph


def create_pp5_statistic():
    confident =0
    not_confident =0
    
    

    for index, row in df.iterrows():
        if(row['PP5a_W49'] == 1 or row['PP5a_W49'] == 2):
            confident +=1
        elif(row['PP5a_W49'] == 3 or row['PP5a_W49'] == 4):
            not_confident +=1

    final_confident = (confident / (confident+not_confident))*100

    return "{}% of Americans are not confident companies will follow their own privacy policies for their data.".format(round(final_confident,1))





def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [
                    html.H5("America\'s Concern Over Facebook"),
                    html.Div([
                        dcc.Graph(figure=create_fb_only_graph(), config= {'displaylogo': False})
                    ]),
                    html.Div([
                        dcc.Graph(figure=create_fb_and_concern_graph(), config= {'displaylogo': False})
                    ]),
                    html.Div([
                        html.H4(create_pp5_statistic(),style={"text-align": "center","background": "#0075FF","color": "#ffffff"})
                    ]),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )