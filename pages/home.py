import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

from packages.db_connect import get_reg_season, get_playoffs

layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                """
                                Men of Madison Fantasy Football League (MoM FFBL)
                                """,
                                className="text-center",
                                style={"color": "#B599CE"},
                            ),
                            className="mb-1",
                            style={"max-width": "90%"},
                        )
                    ],
                    className="justify-content-center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H6(
                                """
                                Welcome! This is a 10-Team league formed in 2012 by the gentlemen of Phi Epsilon Kappa - Delta Gamma Chapter from James Madison University. 
                                """,
                                className="text-left",
                            ),
                            className="mb-3",
                        )
                    ],
                    align="left",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H3(
                                                children="",
                                                className="text-center",
                                                style={"color": "#CBB677"},
                                                id="rankings-header",
                                            )
                                        ]
                                    ),
                                    html.Div(id="reg-season-table"),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            class_name="mb-4",
                        ),
                    ],
                    justify="center",
                    className="mb-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H3(
                                                children="Season Finish",
                                                className="text-center",
                                                style={"color": "#CBB677"},
                                                id="season-finish-header",
                                            )
                                        ]
                                    ),
                                    html.Div(id="season-finish-table"),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            class_name="mb-4",
                        ),
                    ],
                    justify="center",
                ),
            ]
        ),
        dcc.Interval(
            id="home-interval-component",
            interval=3600 * 1000,  # in milliseconds
            n_intervals=0,
        ),
    ]
)


@dash.callback(
    Output("reg-season-table", "children"),
    Output("rankings-header", "children"),
    Output("season-finish-table", "children"),
    Input("home-interval-component", "n_intervals"),
)
def reg_season_table_update(n):
    reg_season = get_reg_season()
    max_reg_week = reg_season["Week"].max()
    reg_season = reg_season[reg_season["Week"] == max_reg_week]
    reg_season = reg_season[reg_season.columns[1:]]
    reg_season_table = dbc.Table.from_dataframe(
        reg_season,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className="table-sm rounded m-2",
    )
    if max_reg_week > 15:
        playoffs = get_playoffs()
        max_playoff_week = playoffs["Week"].max()
        playoffs = playoffs[playoffs["Week"] == max_playoff_week]
        playoffs = playoffs[playoffs.columns[2:6]]
        playoff_table = dbc.Table.from_dataframe(
            playoffs,
            striped=True,
            bordered=False,
            hover=True,
            responsive=True,
            className="table-sm rounded",
        )

    else:
        playoff_table = html.H6(
            "Regular season still active, finish has not been determined.",
            className="m-3",
            style={"color": "#B599CE"},
        )

    return reg_season_table, f"Week {max_reg_week} Rankings", playoff_table
