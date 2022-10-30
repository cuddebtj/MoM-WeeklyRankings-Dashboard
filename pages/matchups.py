import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

# from packages.db_connect import get_reg_season, get_playoffs

app = dash.Dash(
    __name__,
    use_pages=False,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.SLATE],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="MoM-FFbl",
    # assets_folder="static/"
)

server = app.server


def matchup_cards():
    pass


layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                "Matchups",
                                className="text-left",
                                style={"color": "#B599CE"},
                            ),
                        )
                    ],
                    justify="left",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        dbc.Card(
                                                            [
                                                                dbc.CardBody(
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    html.H6(
                                                                                        "Fantasy Sidelines"
                                                                                    ),
                                                                                    html.Span(
                                                                                        "Tim"
                                                                                    ),
                                                                                ],
                                                                                width="auto",
                                                                            ),
                                                                            dbc.Col(
                                                                                html.Span(
                                                                                    "Score1"
                                                                                ),
                                                                                style={
                                                                                    "display": "flex",
                                                                                    "align-items": "center",
                                                                                },
                                                                                width="auto",
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                            ],
                                                            color="dark",
                                                            outline=True,
                                                            style={
                                                                "text-align": "right"
                                                            },
                                                        ),
                                                        class_name="mb-0 text-right",
                                                    ),
                                                    # dbc.Col(html.P("vs."), style={"display": "flex", "align-items": "center"}),
                                                    dbc.Col(
                                                        dbc.Card(
                                                            [
                                                                dbc.CardBody(
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                html.Span(
                                                                                    "Score2"
                                                                                ),
                                                                                style={
                                                                                    "display": "flex",
                                                                                    "align-items": "center",
                                                                                },
                                                                                # width="auto",
                                                                            ),
                                                                            dbc.Col(
                                                                                [
                                                                                    html.H6(
                                                                                        "Poor Decisions 😢"
                                                                                    ),
                                                                                    html.Span(
                                                                                        "Pete"
                                                                                    ),
                                                                                ],
                                                                                width="auto",
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                            ],
                                                            color="dark",
                                                            outline=True,
                                                            style={
                                                                "text-align": "left"
                                                            },
                                                        ),
                                                        class_name="mb-0 text-left",
                                                    ),
                                                ]
                                            ),
                                        ],
                                        title="Week 1",
                                        class_name="rounded",
                                        style={"border-color": "#CBB677"},
                                    ),
                                ],
                                start_collapsed=True,
                                always_open=True,
                            ),
                            width="auto",
                            className="mb-1 rounded",
                        ),
                    ],
                    justify="center",
                    className="mb-2",
                ),
            ]
        ),
        # dcc.Interval(
        #     id="interval-component",
        #     interval=900 * 1000,  # in milliseconds
        #     n_intervals=0,
        # ),
    ]
)

app.layout = layout

# @dash.callback(
#     Output("matcups", "children"), Input("interval-component", "n_intervals")
# )
# def matcups_update(n):
#     reg_season = get_reg_season()
#     reg_season = reg_season[reg_season.columns[1:]]

#     pass
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
