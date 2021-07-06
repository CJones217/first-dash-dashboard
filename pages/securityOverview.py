import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df = pd.read_csv(DATA_PATH.joinpath('master.csv'))

def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div(
                [
                    
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )