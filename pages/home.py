import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

from packages.db_connect import get_reg_season, get_playoffs

playoffs = get_playoffs()
playoff_week = playoffs["Week"].max()

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
                                style={"color": "#B599CE"},
                            ),
                            className="mb-5",
                        )
                    ],
                    align="justify",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H3(
                                                children=f"Week {playoff_week} Rankings",
                                                className="text-center",
                                                style={"color": "#CBB677"},
                                            )
                                        ]
                                    ),
                                    html.Div(id="reg-season-table"),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            class_name="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H3(
                                                children=f"Week {playoff_week} Playoff Picture",
                                                className="text-center",
                                                style={"color": "#CBB677"},
                                            )
                                        ]
                                    ),
                                    html.Div(id="playoff-table"),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            class_name="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-5",
                ),
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=900 * 1000,  # in milliseconds
            n_intervals=0,
        ),
    ]
)


@dash.callback(
    Output("reg-season-table", "children"), Input("interval-component", "n_intervals")
)
def reg_season_table_update(n):
    reg_season = get_reg_season()
    reg_season = reg_season[reg_season["Week"] == reg_season["Week"].max()]
    reg_season = reg_season[reg_season.columns[1:]]
    reg_season_table = dbc.Table.from_dataframe(
        reg_season,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className="table-sm rounded m-2",
    )

    return reg_season_table


@dash.callback(
    Output("playoff-table", "children"), Input("interval-component", "n_intervals")
)
def playoff_table_update(n):
    playoffs = get_playoffs()
    playoffs = playoffs[playoffs["Week"] == playoffs["Week"].max()]
    playoffs = playoffs[playoffs.columns[1:]]
    playoff_table = dbc.Table.from_dataframe(
        playoffs,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className="table-sm rounded m-2",
    )

    return playoff_table
