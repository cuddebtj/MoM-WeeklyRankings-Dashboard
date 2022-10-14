from dash import Dash, dash_table, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
# import dash_twitter_widget

import app

from packages.db_connect import DatabaseCursor


def reg_season_standings():
    reg_season_standings_query = '''
    SELECT "Cur. Wk Rk", 
    "Manager", 
    "Prev. Wk Rk", 
    "2pt Ttl", 
    "Ttl Pts Win", 
    "Win Ttl"||'-'||"Loss Ttl" as "Record", 
    "Ttl Pts", 
    "Ttl Pts Rk", 
    "Wk W/L", 
    "Wk Pts W/L", 
    "Wk Pts", 
    "Wk Pts Rk", 
    "Opp Manager", 
    "Opp Wk Pts", 
    "Avg Pts", 
    "Avg Opp Pts",
    "Ttl Opp Pts" 
    FROM prod.reg_season_results 
    WHERE "Week" = (SELECT max("Week") FROM prod.reg_season_results) 
    ORDER BY "Week", 
    "Cur. Wk Rk"
    '''

    return DatabaseCursor().copy_from_psql(reg_season_standings_query)

def playoffs():
    playoffs_query = '''
    SELECT "Playoff Seed", 
    "Manager", 
    "Bracket", 
    "Wk Pts", 
    "Wk Pro. Pts", 
    "Opp Manager", 
    "Opp Wk Pts", 
    "Opp Wk Pro. Pts", 
    "Wk W/L", 
    "Finish"
    FROM prod.playoff_board 
    ORDER BY "Week", 
    "Finish"
    '''

    return DatabaseCursor().copy_from_psql(playoffs_query)


df_reg_season_standings = reg_season_standings()
df_playoffs = playoffs()


def layout():
    return [
        dbc.Col(
            dbc.Card(
                children=[
                    dbc.CardHeader("Welcome to the prestigious Men of Madison Fantasy Football League (MoM FFL)"),
                    dbc.CardBody(
                        [
                            dcc.Markdown(
                                """
                                This is a 10-Team league formed in 2012 by the gentlemen of Phi Epsilon Kappa - Delta Gamma Chapter from James Madison University. 
                                This is considered a money league and all owners are expected to pay their league dues before the draft begins. 
                                This league is extremely competitive and will be treated as such. There are rules, which are decided based on a voting system. 
                                All changes to articles will require a majority vote (greater than 50%) by all owners.
                                Check [here](https://menofmadisonffbl.slack.com/) for the league slack channel.
                                """,
                                style={"margin": "0 10px"},
                            )
                        ]
                    ),
                ]
            ),
            width=12,
        ),
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Card(
                            children=[
                                dbc.CardHeader("REGULAR SEASON RANKINGS"),
                                dbc.CardBody(
                                    children=[
                                        dash_table.DataTable(
                                            columns=[
                                                {"name": i, "id": i}
                                                for i in df_reg_season_standings.columns
                                            ],
                                            data=df_reg_season_standings.to_dict("records"),
                                            tooltip_header={
                                                "Cur. Wk Rk": "Current Week Rank",
                                                "Prev. Wk Rk": "Previous Week Rank",
                                                "2pt Ttl": "Total Points Scored in the 2 point system",
                                                "Ttl Pts Win": "Total Wins against league median",
                                                "Record": "Total Wins in Head-to-Head used for 2 point system",
                                                "Ttl Pts": "Total Points Scored this season, also the tie breaker for 2pt Ttl",
                                            },
                                            # style_data={
                                            #     'whiteSpace': 'normal',
                                            #     'height': 'auto',
                                            # },
                                            style_table={'minWidth': '100%'},
                                            style_header={
                                                "fontWeight": "bold",
                                                "whiteSpace": 'normal', 
                                                "height": 'auto',
                                                "textAlign": "left",
                                            },
                                            style_header_conditional=[{
                                                'if': {'column_id': col},
                                                'textDecoration': 'underline',
                                                'textDecorationStyle': 'dotted',
                                            } for col in ['Cur. Wk Rk', 'Prev. Wk Rk', '2pt Ttl', "Ttl Pts Win", "Record", "Ttl Pts"]],
                                            style_cell={
                                                "textAlign": "center",
                                                "font-size": "14px",
                                                "minWidth": 50, 
                                                "maxWidth": 100, 
                                                "width": 80,
                                            },
                                            fixed_columns={'headers': True, 'data': 2},
                                            style_cell_conditional=[
                                                {
                                                    "if": {"column_id": ["Manager", "Opp Manager"]},
                                                    "textAlign": "left",
                                                }
                                            ],
                                            style_as_list_view=True,
                                            sort_action='native',
                                            tooltip_delay=0,
                                            tooltip_duration=None,
                                            css=[{
                                                'selector': '.dash-table-tooltip',
                                                'rule': 'background-color: grey; font-family: monospace; color: white; font-size: 12px;'
                                            }],
                                        )
                                    ],
                                    class_name="dbc",
                                ),
                            ]
                        ),
                        dbc.Card(
                            children=[
                                dbc.CardHeader("PLAYOFF RANKINGS"),
                                dbc.CardBody(
                                    children=[
                                        dash_table.DataTable(
                                            columns=[
                                                {"name": i, "id": i}
                                                for i in df_playoffs.columns
                                            ],
                                            data=df_playoffs.to_dict(
                                                "records"
                                            ),
                                            # style_data={
                                            #     'whiteSpace': 'normal',
                                            #     'height': 'auto',
                                            # },
                                            style_table={'overflowX': 'auto'},
                                            style_header={
                                                "fontWeight": "bold",
                                                "whiteSpace": 'normal', 
                                                "height": 'auto',
                                                "textAlign": "left",
                                            },
                                            style_cell={
                                                "textAlign": "center",
                                                "font-size": "14px",
                                                "minWidth": 50, 
                                                "maxWidth": 100, 
                                                "width": 80,
                                            },
                                            fixed_columns={'headers': True, 'data': 2},
                                            style_cell_conditional=[
                                                {
                                                    "if": {"column_id": ["Manager", "Bracket", "Opp Manager"]},
                                                    "textAlign": "left",
                                                }
                                            ],
                                            style_as_list_view=True,
                                            sort_action='native',
                                        )
                                    ],
                                    class_name="dbc",
                                ),
                            ]
                        ),
                        # dbc.Card(
                        #     children=[
                        #         dash_twitter_widget.DashTwitterWidget(
                        #             id="input", value="SkySportsF1"
                        #         )
                        #     ]
                        # ),
                    ]
                )
            ],
            style={"padding-left": "15px", "padding-right": "15px"},
            className="dbc",
        ),
    ]