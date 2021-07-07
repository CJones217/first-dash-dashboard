import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    securityOverview,
    overview,
    facebook,
    facialRec,
    questionnaire
)

app = dash.Dash( #i prob don't need the tags
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "U.S. Citizens Outlook on Data Privacy and Security"
server = app.server

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/apple-dashboard/security-overview":
        #securityOverview.create_secur_graph()
        return securityOverview.create_layout(app)
    elif pathname == "/apple-dashboard/overview":
        return overview.create_layout(app)
    elif pathname == "/apple-dashboard/facebook":
        return facebook.create_layout(app)
    elif pathname == "/apple-dashboard/facial-recognition":
        return facialRec.create_layout(app)
    elif pathname == "/apple-dashboard/questionnaire":
        return questionnaire.create_layout(app)
    else:
        return overview.create_layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)