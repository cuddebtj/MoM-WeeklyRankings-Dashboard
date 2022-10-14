from ctypes import alignment
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Dash, Input, Output, State, callback

from app import app

import pages

server = app.server

JMU_LOGO = "https://www.jmu.edu/identity/_files/JMU-Logo-RGB-vert-purple.png"

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Header(
            dbc.Navbar(
                children=[
                    dbc.Col(
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            dbc.Row(
                                [
                                html.Img(
                                        src=JMU_LOGO,
                                        style={
                                            "height": "80px", 
                                            "width": "auto",
                                        },
                                    ),
                                    dbc.NavbarBrand(
                                        "Men of Madison Fantasy Football League", 
                                        style={"alignment": "center"},
                                        class_name="dbc",
                                    ),
                                ],
                                class_name="g-0 dbc ml-auto flex-nowrap mt-3 mt-md-0",
                                align="center",
                            ),
                            href=app.get_relative_path("/"),
                        ),
                    ),
                    dbc.Col(
                        dbc.Nav(
                            children=[
                                dbc.NavItem(dbc.NavLink("Home", href=app.get_relative_path("/"))),
                                dbc.NavItem(dbc.NavLink("Bylaws", href=app.get_relative_path("/bylaws"))),
                                dbc.NavItem(dbc.NavLink("Drafts", href=app.get_relative_path("/drafts"))),
                                dbc.NavItem(dbc.NavLink("Seasons", href=app.get_relative_path("/seasons"))),
                                dbc.NavItem(dbc.NavLink("Managers", href=app.get_relative_path("/managers"))),
                                dbc.NavItem(dbc.NavLink("Records", href=app.get_relative_path("/records"))),
                            ],
                            style={
                                "paddingLeft": "65%",
                                "alignment": "center"
                            },
                        ),
                        class_name="g-0 dbc ml-auto flex-nowrap mt-3 mt-md-0",
                    ),
                    
                ]
            ),
            className="dbc",
            style={
                "height": "100px",
            }
        ),
        html.Div(id="page-content"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page_content(pathname):
    path = app.strip_relative_path(pathname)
    if not path:
        return pages.home.layout()
    elif path == "bylaws":
        return pages.bylaws.layout()
    elif path == "drafts":
        return pages.drafts.layout()
    elif path == "seasons":
        return pages.seasons.layout()
    elif path == "managers":
        return pages.managers.layout()
    elif path == "records":
        return pages.records.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)