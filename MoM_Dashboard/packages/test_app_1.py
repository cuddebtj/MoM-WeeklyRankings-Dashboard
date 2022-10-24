import pandas as pd
import plotly
import plotly.express as px

from dash import dcc, html, dash_table, Dash, Input, Output, callback

from db_connect import DatabaseCursor

weekly_rankings_query = """
SELECT "Week", 
"Manager", 
"Cur. Wk Rk", 
"Prev. Wk Rk", 
"2pt Ttl", 
"2pt Ttl Rk", 
"Ttl Pts Win", 
"Ttl Pts Win Rk", 
"Win Ttl",
"Loss Ttl",  
"W/L Rk", 
"Wk W/L", 
"Wk Pts W/L", 
"Wk Pts", 
"Wk Pts Rk", 
"Wk Pro. Pts", 
"Opp Manager", 
"Opp Wk Pts", 
"Opp Wk Pts Rk", 
"Opp Wk Pro. Pts",  
"Avg Pts", 
"Avg Pts Rk", 
"Avg Opp Pts", 
"Avg Opp Pts Rk", 
"Ttl Pts", 
"Ttl Pts Rk", 
"Ttl Pro. Pts", 
"Ttl Pro. Pts Rk", 
"Ttl Opp Pts", 
"Ttl Opp Pts Rk", 
"Ttl Opp Pro. Pts", 
"Ttl Opp Pro. Pts Rk"
FROM prod.reg_season_results
ORDER BY "Week", 
"Cur. Wk Rk"
"""

weekly_rankings_df = DatabaseCursor().copy_from_psql(weekly_rankings_query)

playoffs_query = """
SELECT "Week", 
"Bracket", 
"Manager", 
"Finish", 
"Playoff Seed", 
"Wk W/L", 
"Wk Pts", 
"Wk Pro. Pts", 
"Opp Manager", 
"Opp Wk Pts", 
"Opp Wk Pro. Pts",  
"Ttl Pts", 
"Ttl Pro. Pts", 
"Opp Ttl Pts", 
"Opp Ttl Pro. Pts"
FROM prod.playoff_board
ORDER BY "Week", 
"Finish"
"""

playoffs_df = DatabaseCursor().copy_from_psql(playoffs_query)

week_list = list(weekly_rankings_df["Week"].unique())
week_list.sort()
max_weekly_week = weekly_rankings_df["Week"].max()
managers = list(weekly_rankings_df["Manager"].unique())
managers.sort()
playoff_weeks = list(playoffs_df["Week"].unique())
playoff_weeks.sort()
max_playoff_week = playoffs_df["Week"].max()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Men Of Madison Fantasy Football League"),
                html.H2("Weekly Rankings - 2 Point System"),
                html.Div(
                    [
                        dcc.Dropdown(week_list, max_weekly_week, clearable=True),
                        dcc.Dropdown(managers, "", multi=True, clearable=True),
                    ]
                ),
                dash_table.DataTable(
                    id="Weekly_Rankings",
                    data=weekly_rankings_df.to_dict("records"),
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": False}
                        for i in weekly_rankings_df.columns
                    ],
                    page_size=10,
                    fixed_rows={"headers": True},
                    style_table={"height": 400},
                    style_cell={
                        "minWidth": 25,
                        "maxWidth": 75,
                        "width": 65,
                        "textAlign": "center",
                    },
                    style_header={
                        "whiteSpace": "normal",
                        "height": "auto",
                        "fontWeight": "bold",
                        "backgroundColor": "rgb(210, 210, 210)",
                    },
                    style_as_list_view=True,
                    style_data_conditional=[
                        {
                            "if": {"row_index": "odd"},
                            "backgroundColor": "rgb(220, 220, 220)",
                        }
                    ],
                ),
            ]
        ),
        html.Div(
            [
                html.H2("Current Playoff Picture Head to Head"),
                html.Div(
                    [
                        dcc.Dropdown(playoff_weeks, max_playoff_week, clearable=True),
                        dcc.Dropdown(managers, "", multi=True, clearable=True),
                    ]
                ),
                dash_table.DataTable(
                    id="Playoffs",
                    data=playoffs_df.to_dict("records"),
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": False}
                        for i in playoffs_df.columns
                    ],
                    page_size=10,
                    fixed_rows={"headers": True},
                    style_table={"height": 350},
                    style_cell={
                        "minWidth": 25,
                        "maxWidth": 75,
                        "width": 65,
                        "textAlign": "center",
                    },
                    style_header={
                        "whiteSpace": "normal",
                        "height": "auto",
                        "fontWeight": "bold",
                        "backgroundColor": "rgb(210, 210, 210)",
                    },
                    # style_cell_conditional=[
                    #     {'if': {'column_id': 'Temperature'},
                    #     'width': '130px',
                    #     'textAlign': 'left'},
                    #     {'if': {'column_id': 'Humidity'},
                    #     'width': '130px'},
                    #     {'if': {'column_id': 'Pressure'},
                    #     'width': '130px'},
                    style_as_list_view=True,
                    style_data_conditional=[
                        {
                            "if": {"row_index": "odd"},
                            "backgroundColor": "rgb(220, 220, 220)",
                        }
                    ],
                ),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
