import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from whitenoise import WhiteNoise

from pages import home, bylaws, drafts, managers, matchups, records, seasons

app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.SLATE],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="MoM-FFbl",
    # assets_folder="static/"
)

server = app.server

server.wsgi_app = WhiteNoise(server.wsgi_app, root="static/")

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(
            [
                html.Img(
                    src="https://www.jmu.edu/identity/_files/jmu-logo-rgb-vert-purple.png",
                    alt="JMU-Logo",
                    style={"width": "100%"},
                ),
                html.H4("2022", style={"text-align": "right"}),
            ],
            style={},
        ),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(203, 182, 119, 0.5)",
                        "border-color": "rgba(69, 0, 132, 0.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(203, 182, 119, 0.5)",
                        "border-color": "rgba(9, 0, 132, 0.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.H4(
                    "Men of Madison Fantasy Football League",
                    className="font-weight-bold",
                    style={"color": "#450084"},
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink(
                        "Home", href="/", active="exact", style={"color": "#B599CE"}
                    ),
                    dbc.NavLink(
                        "Bylaws",
                        href="/bylaws",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Matchups",
                        href="/matchups",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Drafts",
                        href="/drafts",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Managers",
                        href="/managers",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Seasons",
                        href="/seasons",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Records",
                        href="/records",
                        active="exact",
                        style={"color": "#B599CE"},
                    ),
                    dbc.NavLink(
                        "Yahoo League",
                        href="https://football.fantasysports.yahoo.com/f1/77446",
                        active="exact",
                        style={"color": "#CBB677"},
                    ),
                    dbc.NavLink(
                        "Slack Channel",
                        href="https://app.slack.com/client/TLC9R6Q7Q",
                        active="exact",
                        style={"color": "#CBB677"},
                    ),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout

    elif pathname == "/bylaws":
        return bylaws.layout

    elif pathname == "/matchups":
        return matchups.matchup_page

    elif pathname == "/drafts":
        return html.Div(
            [
                html.H1("Drafts build in progress. ", className="text-danger"),
                html.Hr(),
                html.P("Patience is a virtue."),
            ],
            className="p-3 bg-light rounded-3",
        )

    elif pathname == "/managers":
        return html.Div(
            [
                html.H1("Managers build in progress. ", className="text-danger"),
                html.Hr(),
                html.P(
                    "Patience, first we lure them in with intrigue, then we RULE THEM!!"
                ),
            ],
            className="p-3 bg-light rounded-3",
        )

    elif pathname == "/seasons":
        return html.Div(
            [
                html.H1("Seasons build in progress. ", className="text-danger"),
                html.Hr(),
                html.P("I had my patience tested, it came up negative."),
            ],
            className="p-3 bg-light rounded-3",
        )

    elif pathname == "/records":
        return html.Div(
            [
                html.H1("Records build in progress. ", className="text-danger"),
                html.Hr(),
                html.P(
                    "Lord give me patience because if you give me strength, I'm gonna need bail money! Chill bro."
                ),
            ],
            className="p-3 bg-light rounded-3",
        )

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    # app.run_server(debug=True, host="0.0.0.0", port=8050)
    app.run_server(debug=False,  host="0.0.0.0", port=8050)
