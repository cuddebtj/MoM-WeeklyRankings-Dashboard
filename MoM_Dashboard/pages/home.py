import dash
from dash import html
import dash_bootstrap_components as dbc

from packages.db_connect import get_reg_season, get_playoffs

reg_season = get_reg_season()
max_week = reg_season["Week"].max()
reg_season = reg_season[reg_season["Week"] == max_week]
reg_season = reg_season[reg_season.columns[1:]]
reg_season_table = dbc.Table.from_dataframe(
    reg_season, striped=True, bordered=True, hover=True, responsive=True
)

playoffs = get_playoffs()
playoff_week = playoffs["Week"].max()
playoffs = playoffs[playoffs["Week"] == playoff_week]
playoffs = playoffs[playoffs.columns[1:]]
playoff_table = dbc.Table.from_dataframe(
    playoffs, striped=True, bordered=True, hover=True, responsive=True
)

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
                                style={"color": "#CBB677"},
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
                                                children=f"Week {max_week} Rankings",
                                                className="text-center",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    reg_season_table,
                                ],
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
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H3(
                                                children=f"Week {playoff_week} Playoff Picture",
                                                className="text-center",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    playoff_table,
                                ],
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
