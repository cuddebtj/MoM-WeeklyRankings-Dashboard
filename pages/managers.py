# import dash
# from dash import html, Input, Output, dcc
# import dash_bootstrap_components as dbc

# from packages.db_connect import get_reg_season, get_playoffs

# def matchup_cards():
#     pass

# layout = html.Div(
#     [
#         dbc.Container(
#             [
#                 dbc.Row(
#                     [
#                         dbc.Col(
#                             html.H1(
#                                 "Matchups",
#                                 className="text-left",
#                                 style={"color": "#B599CE"},
#                             ),
#                         )
#                     ],
#                     justify="left",
#                 ),
#                 dbc.Row(
#                     [
#                         dbc.Col(
#                             dbc.Accordion(
#                                 [
#                                     dbc.AccordionItem(
#                                         [
#                                             html.P(
#                                                 """
#                                                 Matchup here
#                                                 """,
#                                                 style={"padding": "10px"},
#                                             ),
#                                         ],
#                                         title="Week 1",
#                                         class_name="rounded",
#                                         style={"border-color": "#CBB677"},
#                                     ),
#                                 ],
#                                 start_collapsed=True,
#                                 always_open=True,
#                             ),
#                             width="auto",
#                             className="mb-1 rounded",
#                         ),
#                     ],
#                     justify="center",
#                     className="mb-2",
#                 ),
#             ]
#         ),
#         dcc.Interval(
#             id="interval-component",
#             interval=900 * 1000,  # in milliseconds
#             n_intervals=0,
#         ),
#     ]
# )


# @dash.callback(
#     Output("matcups", "children"), Input("interval-component", "n_intervals")
# )
# def matcups_update(n):
#     reg_season = get_reg_season()
#     reg_season = reg_season[reg_season.columns[1:]]

#     pass
