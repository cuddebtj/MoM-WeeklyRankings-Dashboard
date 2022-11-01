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
                                                    html.Div(
                                                        dbc.Card(
                                                            [
                                                                dbc.CardBody(
                                                                    dbc.Row(
                                                                        [
                                                                            html.Div(
                                                                                [
                                                                                    "Fantasy Sidelines",
                                                                                    html.Div(
                                                                                        "Tim",
                                                                                        style={"font-size": "0.7em",
                                                                                        "font-style": "italic"}
                                                                                    ),
                                                                                ],
                                                                                style={
                                                                                    "margin": "0",
                                                                                    "font-size": "1em",
                                                                                    "line-height": "1.1em",
                                                                                    "flex-grow": "1",
                                                                                    "word-break": "break-word",
                                                                                },
                                                                            ),
                                                                            html.Div(
                                                                                [
                                                                                    "115.15",
                                                                                    html.Div(
                                                                                        "110.8",
                                                                                        style={"font-size": "0.7em",
                                                                                        "font-style": "italic"}
                                                                                    ),
                                                                                ],
                                                                                style={"line-height": "1.1em",
                                                                                "margin-left": "0.1em",
                                                                                "text-align": "right"}
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            color="dark",
                                                            outline=True,
                                                            style={"justify-content": "flex-end",
                                                                "right": "0",
                                                                "text-align": "right",}
                                                        ),
                                                        className="mb-0",
                                                            style={
                                                                
                                                                "display": "flex",
                                                                            "align-items": "center",
                                                                            "width": "46%",
                                                                            "padding": "5px 2%",
                                                                            "top": "0",
                                                                            "z-index": "2",
                                                            },
                                                    ),
                                                    # dbc.Col(html.P("vs."), style={"display": "flex", "align-items": "center"}),
                                                    html.Div(
                                                        dbc.Card(
                                                            [
                                                                dbc.CardBody(
                                                                    dbc.Row(
                                                                        [
                                                                            html.Div(
                                                                                [
                                                                                    "Fantasy Sidelines",
                                                                                    html.Div(
                                                                                        "Tim",
                                                                                        style={"font-size": "0.7em",
                                                                                        "font-style": "italic"}
                                                                                    ),
                                                                                ],
                                                                                style={
                                                                                    "margin": "0",
                                                                                    "font-size": "1em",
                                                                                    "line-height": "1.1em",
                                                                                    "flex-grow": "1",
                                                                                    "word-break": "break-word",
                                                                                },
                                                                            ),
                                                                            html.Div(
                                                                                [
                                                                                    "115.15",
                                                                                    html.Div(
                                                                                        "110.8",
                                                                                        style={"font-size": "0.7em",
                                                                                        "font-style": "italic"}
                                                                                    ),
                                                                                ],
                                                                                style={"line-height": "1.1em",
                                                                                "margin-right": "0.1em",
                                                                                "text-align": "left"}
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            color="dark",
                                                            outline=True,
                                                            style={"justify-content": "flex-start",
                                                                "left": "0",
                                                                "text-align": "left",}
                                                        ),
                                                        className="mb-0",
                                                            style={
                                                                
                                                                "display": "flex",
                                                                            "align-items": "center",
                                                                            "width": "46%",
                                                                            "padding": "5px 2%",
                                                                            "top": "0",
                                                                            "z-index": "2",
                                                            },
                                                    ),
                                                ],
                                                style={
                                                    "display": "flex",
                                                    "justify-content": "space-between",
                                                    "psoition": "relative",
                                                    "border": "1px solid",
                                                    "border-radius": "10px",
                                                    "opacity": "0.8",
                                                },
                                            ),
                                        ],
                                        title="Week 1",
                                        class_name="rounded",
                                        style={
                                            "border-color": "#CBB677",
                                            "width": "95%",
                                            "max-width": "600px",
                                            "margin": "10px auto",
                                        },
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
