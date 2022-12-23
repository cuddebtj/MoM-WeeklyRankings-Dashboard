import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

from packages.db_connect import prod_playoff_board_tbl, prod_reg_season_results_tbl

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
                                    html.Div(
                                        id="reg-season-table",
                                        className="justify-content-center",
                                    ),
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
                                    html.Div(
                                        id="season-finish-table",
                                        className="justify-content-center",
                                    ),
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
            interval=300 * 1000,  # in milliseconds
            n_intervals=0,
        ),
    ]
)


@dash.callback(
    Output("rankings-header", "children"),
    Output("reg-season-table", "children"),
    Output("season-finish-header", "children"),
    Output("season-finish-table", "children"),
    Input("home-interval-component", "n_intervals"),
)
def home_updates(n):
    reg_season = prod_reg_season_results_tbl()
    reg_season = reg_season[
        [
            "Week",
            "Prev. Wk Rk",
            "Manager",
            "Team",
            "Cur. Wk Rk",
            "2pt Ttl",
            "Ttl Pts Win",
            "Win Ttl",
            "Loss Ttl",
            "Ttl Pts",
            "Ttl Pts Rk",
        ]
    ]
    max_reg_week = reg_season["Week"].max()

    if max_reg_week == 15:
        reg_season.sort_values(["Week", "Cur. Wk Rk"], inplace=True)
        reg_season_table_title = f"End of {max_reg_week} Rankings"
    else:
        reg_season.sort_values(["Week", "Prev. Wk Rk"], inplace=True)
        reg_season_table_title = f"Week {max_reg_week} Rankings"

    reg_season = reg_season[reg_season["Week"] == max_reg_week]
    reg_season = reg_season[reg_season.columns[1:]]
    reg_season_table = dbc.Table.from_dataframe(
        reg_season,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className="reg-season-table table-sm rounded m-2",
        id="reg_season_table",
    )

    playoffs_table_title = "Season Finish"

    if max_reg_week >= 15:
        playoffs = prod_playoff_board_tbl()
        max_playoff_week = playoffs["Week"].max()
        playoffs = playoffs[playoffs["Week"] == max_playoff_week]
        playoffs["Bracket"] = playoffs["Bracket"].replace(
            ["Reg Season Finish"], ["Bye"]
        )

        if max_playoff_week == 17:
            playoffs = playoffs[
                [
                    "Finish",
                    "Manager",
                    "Team",
                    "Playoff Seed",
                ]
            ].sort_values(["Finish"])
            playoff_table = dbc.Table.from_dataframe(
                playoffs,
                striped=True,
                bordered=False,
                hover=True,
                responsive=True,
                className="season-finish-table table-sm rounded",
                id="playoff_table_finish",
            )
        else:
            playoffs = playoffs[
                [
                    "Playoff Seed",
                    "Manager",
                    "Bracket",
                    "Opp Manager",
                ]
            ].sort_values(["Playoff Seed"])
            playoffs_table_title = "Semi Finals!"
            playoff_table = dbc.Table.from_dataframe(
                playoffs,
                striped=True,
                bordered=False,
                hover=True,
                responsive=True,
                className="season-finish-table table-sm rounded",
                id="playoff_table_semis",
            )

    else:
        playoff_table = html.H6(
            "Regular season still active, finish has not been determined.",
            className="m-3",
            style={"color": "#B599CE"},
        )

    return reg_season_table_title, reg_season_table, playoffs_table_title, playoff_table
