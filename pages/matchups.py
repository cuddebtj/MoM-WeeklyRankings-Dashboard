import dash
from dash import html, Input, Output, dcc
import dash_bootstrap_components as dbc

from packages.db_connect import get_matchups

reg_season = get_matchups()

matches_merged = reg_season.merge(
    reg_season,
    left_on=["team_key", "Week"],
    right_on=["opp_team_key", "Week"],
    suffixes=("", "_opp"),
)

matchups = matches_merged[
    [
        "Week",
        "team_key",
        "Prev. Wk Rk",
        "Manager",
        "Team",
        "Wk Pts",
        "Wk Pro. Pts",
        "opp_team_key",
        "Prev. Wk Rk_opp",
        "Opp Manager",
        "Opp Team",
        "Opp Wk Pts",
        "Opp Wk Pro. Pts",
    ]
][
    (matches_merged["Prev. Wk Rk"] < matches_merged["Prev. Wk Rk_opp"])
    | (
        (matches_merged["team_key"] < matches_merged["opp_team_key"])
        & (matches_merged["Week"] == 1)
    )
]

matchups.reset_index(drop=True, inplace=True)
max_week = matchups["Week"].max()
current_week = f"Week {max_week}"
dropdown_options = [f"Week {wk}" for wk in matchups["Week"].unique()]


def matchup_card(
    home_team,
    home_manager,
    home_pts,
    home_pro_pts,
    home_rk,
    away_team,
    away_manager,
    away_pts,
    away_pro_pts,
    away_rk,
):
    return html.Div(
        [
            html.Div(
                [
                    html.Img(
                        className="avatar",
                        src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/pile-of-poo_1f4a9.png",
                        alt="Poop",
                    ),
                    html.Div(
                        [
                            home_team,
                            html.Div(
                                f"{home_manager} ({home_rk})",
                                className="totalProjection",
                            ),
                        ],
                        className="name",
                    ),
                    html.Div(
                        [home_pts, html.Div(home_pro_pts, className="totalProjection")],
                        className="totalPoints totalPointsR",
                    ),
                ],
                className="opponent home",
            ),
            html.Div(
                [
                    html.Div(
                        [away_pts, html.Div(away_pro_pts, className="totalProjection")],
                        className="totalPoints totalPointsL",
                    ),
                    html.Div(
                        [
                            away_team,
                            html.Div(
                                f"{away_manager} ({away_rk})",
                                className="totalProjection",
                            ),
                        ],
                        className="name",
                    ),
                    html.Img(
                        className="avatar",
                        src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/pile-of-poo_1f4a9.png",
                        alt="Poop",
                    ),
                ],
                className="opponent away",
            ),
        ],
        className="header",
    )

def matchups_layout(matchups, week):
    matchups_week = matchups[matchups['Week'] == week]
    matchup_layout = []

    for index, match in matchups_week.iterrows():
        home_team = match["Opp Team"]
        home_manager = match["Opp Manager"]
        home_pts = match["Opp Wk Pts"]
        home_pro_pts = match["Opp Wk Pro. Pts"]
        home_rk = match["Prev. Wk Rk_opp"]
        away_team = match["Team"]
        away_manager = match["Manager"]
        away_pts = match["Wk Pts"]
        away_pro_pts = match["Wk Pro. Pts"]
        away_rk = match["Prev. Wk Rk"]
        matchup_layout.append(
            matchup_card(
                home_team,
                home_manager,
                home_pts,
                home_pro_pts,
                home_rk,
                away_team,
                away_manager,
                away_pts,
                away_pro_pts,
                away_rk,
            )
        )

    return matchup_layout

matchup_page = html.Div(
    html.Div(
        [
            html.Div(
                html.H1("Matchups", className="weekText", style={"color": "#B599CE"}),
                className="weekContainer",
            ),
            html.Div(
                dcc.Dropdown(
                    dropdown_options,
                    value=current_week,
                    id="matchups-dropdown",
                    placeholder="Week",
                    className="drop-down",
                    clearable=False,
                    searchable=False,
                ),
                className="drop-down-matchups",
            ),
            html.Div(matchups_layout(matchups, max_week), className="matchup", id="vis-matchups"),
        ],
        className="matchups",
    ),
    className="main",
)


@dash.callback(
    Output("vis-matchups", "children"),
    Input("matchups-dropdown", "value"),
)
def matcups_update(value):
    if value:
        week = int(value[5:])
    matchup_layout = matchups_layout(matchups, week)
    return matchup_layout


# @dash.callback(
#     Output("dropdown", "value"),
#     Input("dropdown", "value"),
# )
# def change_page(value):
#     if value:
#         return value
#     return "Week 10"
