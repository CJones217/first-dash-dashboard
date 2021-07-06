import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    securityOverview,
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
        return securityOverview.create_layout(app)
    else:
        return securityOverview.create_layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)