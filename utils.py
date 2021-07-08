import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("signal.png"),
                            className="logo",
                        ),
                        href="https://collinjones.xyz",
                    ),
                    html.A(
                        html.Button(
                            "visit my website!",
                            id="learn-more-button",
                            style={"margin-left": "-10px"},
                        ),
                        href="https://collinjones.xyz",
                    ),
                    html.A(
                        html.Button("Source Code", id="learn-more-button"),
                        href="https://github.com/CJones217/first-dash-dashboard",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("U.S. Privacy Report")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/apple-dashboard/overview",
                className="tab first", 
            ),
            dcc.Link(
                "Questionnaire", 
                href="/apple-dashboard/questionnaire",  
                className="tab", 
            ),
            dcc.Link(
                "Security Overview", 
                href="/apple-dashboard/security-overview",  
                className="tab", 
            ),
            dcc.Link(
                "Facebook", 
                href="/apple-dashboard/facebook", 
                className="tab", 
            ),
        ],
        className="row all-tabs", 
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table