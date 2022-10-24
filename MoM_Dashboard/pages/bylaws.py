import dash
from dash import html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                "Welcome to the Men of Madison Fantasy Football League!",
                                className="text-center",
                            ),
                            className="mb-5 mt-5",
                        )
                    ],
                    justify="center",
                ),
                dbc.Row([dbc.Col(html.H5(children=""), className="mb-4")]),
                dbc.Row([dbc.Col(html.H5(children=""), className="mb-5")]),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Get the original datasets used in this dashboard",
                                        className="text-center",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Get the original datasets used in this dashboard",
                                        className="text-center",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Get the original datasets used in this dashboard",
                                        className="text-center",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-5",
                ),
            ]
        )
    ]
)
