import dash
import pandas as pd
from dash import html, Input, Output, dcc, ctx
import dash_bootstrap_components as dbc

from packages.db_connect import get_matchups, get_playoffs


def reg_season_matchups():
    reg_season = get_matchups()
    m_week = reg_season["Week"].max()
    matches_merged = reg_season.merge(
        reg_season,
        left_on=["team_key", "Week"],
        right_on=["opp_team_key", "Week"],
        suffixes=("", "_opp"),
    )

    matches_merged['Week'] = "Week " + matches_merged['Week'].astype(str)
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
            & (matches_merged["Week"] == "Week 1")
        )
    ]

    matchups.reset_index(drop=True, inplace=True)
    max_week = f"Week {m_week}"
    dropdown_options = [wk for wk in matchups["Week"].unique()]
    po_matchups = None
    # conso_matchups = None
    # toilet_matchups = None

    if m_week > 15:
        playoffs = get_playoffs()
        m_week = playoffs["Week"].max()
        playoffs_merged = playoffs.merge(
            playoffs,
            left_on=["team_key", "Week"],
            right_on=["opp_team_key", "Week"],
            suffixes=("", "_opp"),
        )
        playoffs_merged['Week'] = "Round " + playoffs_merged['Week'].astype(str)
        po_matchups = playoffs_merged[
            [
                "Week",
                "team_key",
                "Playoff Seed",
                "Manager",
                "Team",
                "Wk Pts",
                "Wk Pro. Pts",
                "opp_team_key",
                "Playoff Seed_opp",
                "Opp Manager",
                "Opp Team",
                "Opp Wk Pts",
                "Opp Wk Pro. Pts",
                "Bracket",
            ]
        ][
            (playoffs_merged["Playoff Seed"] < playoffs_merged["Playoff Seed_opp"])
            # & (playoffs_merged["Bracket"].str.contains("Play"))
        ]

        # conso_matchups = playoffs_merged[
        #     [
        #         "Week",
        #         "team_key",
        #         "Playoff Seed",
        #         "Manager",
        #         "Team",
        #         "Wk Pts",
        #         "Wk Pro. Pts",
        #         "opp_team_key",
        #         "Playoff Seed_opp",
        #         "Opp Manager",
        #         "Opp Team",
        #         "Opp Wk Pts",
        #         "Opp Wk Pro. Pts",
        #         "Bracket",
        #     ]
        # ][
        #     (playoffs_merged["Playoff Seed"] < playoffs_merged["Playoff Seed_opp"])
        #     & (playoffs_merged["Bracket"].str.contains("Conso"))
        # ]

        # toilet_matchups = playoffs_merged[
        #     [
        #         "Week",
        #         "team_key",
        #         "Playoff Seed",
        #         "Manager",
        #         "Team",
        #         "Wk Pts",
        #         "Wk Pro. Pts",
        #         "opp_team_key",
        #         "Playoff Seed_opp",
        #         "Opp Manager",
        #         "Opp Team",
        #         "Opp Wk Pts",
        #         "Opp Wk Pro. Pts",
        #         "Bracket",
        #     ]
        # ][
        #     (playoffs_merged["Playoff Seed"] < playoffs_merged["Playoff Seed_opp"])
        #     & (playoffs_merged["Bracket"].str.contains("Toilet"))
        # ]

        matchups = pd.concat(
            [
                matchups, 
                po_matchups, 
                # conso_matchups, 
                # toilet_matchups
            ]
        )

        matchups["Prev. Wk Rk"] = matchups["Prev. Wk Rk"].fillna(matchups["Playoff Seed"]).astype(int)
        matchups["Prev. Wk Rk_opp"] = matchups["Prev. Wk Rk_opp"].fillna(matchups["Playoff Seed_opp"]).astype(int)

        for w in playoffs_merged["Week"].unique():
            dropdown_options.append(w)

        max_week = f"Round {m_week}"

    return (
        matchups,
        max_week,
        dropdown_options,
        # po_matchups,
        # conso_matchups,
        # toilet_matchups,
    )


def matchup_card(
    home_team,
    home_manager,
    home_pts,
    home_pro_pts,
    home_rk,
    home_src,
    away_team,
    away_manager,
    away_pts,
    away_pro_pts,
    away_rk,
    away_src,
):
    away_glow = ""
    home_glow = ""
    if home_pts < away_pts:
        away_glow = "awayGlow"
    else:
        home_glow = "homeGlow"
    return html.Div(
        [
            html.Div(
                [
                    html.Img(
                        className="avatar",
                        src=away_src,
                        alt="Poop",
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
                    html.Div(
                        [away_pts, html.Div(away_pro_pts, className="totalProjection")],
                        className="totalPoints totalPointsR",
                    ),
                ],
                className=f"opponent away {away_glow}",
            ),
            html.Div(
                [
                    html.Div(
                        [home_pts, html.Div(home_pro_pts, className="totalProjection")],
                        className="totalPoints totalPointsL",
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
                    html.Img(
                        className="avatar",
                        src=home_src,
                        alt="Poop",
                    ),
                ],
                className=f"opponent home {home_glow}",
            ),
        ],
        className="header mb-2",
    )


def matchups_layout(matchups, week):
    matchups_week = matchups[matchups["Week"] == week]
    match_layout = []
    srcs = {
            "Pete": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/crying-face_1f622.png",
            "Chris": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/x-ray_1fa7b.png",
            "Tim": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/72/apple/325/crown_1f451.png",
            "Pat": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/pill_1f48a.png",
            "Greg": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/new-moon-face_1f31a.png",
            "Wes": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/bar-chart_1f4ca.png",
            "Carter": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/72/apple/325/flying-saucer_1f6f8.png",
            "Kevin": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/man-lifting-weights_1f3cb-fe0f-200d-2642-fe0f.png",
            "Ryan": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/man-health-worker_1f468-200d-2695-fe0f.png",
            "Jeremy": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/bear_1f43b.png",
        }

    for index, match in matchups_week.iterrows():
        home_team = match["Team"]
        home_manager = match["Manager"]
        home_pts = match["Wk Pts"]
        home_pro_pts = match["Wk Pro. Pts"]
        home_rk = match["Prev. Wk Rk"]
        home_src = srcs[match["Manager"]]
        away_team = match["Opp Team"]
        away_manager = match["Opp Manager"]
        away_pts = match["Opp Wk Pts"]
        away_pro_pts = match["Opp Wk Pro. Pts"]
        away_rk = match["Prev. Wk Rk_opp"]
        away_src = srcs[match["Opp Manager"]]
        match_layout.append(
            matchup_card(
                home_team,
                home_manager,
                home_pts,
                home_pro_pts,
                home_rk,
                home_src,
                away_team,
                away_manager,
                away_pts,
                away_pro_pts,
                away_rk,
                away_src,
            )
        )

    return match_layout


(
    matchups,
    max_week,
    dropdown_options,
    # po_matchups,
    # conso_matchups,
    # toilet_matchups,
) = reg_season_matchups()

matchup_page = html.Div(
    [
        html.Div(
            html.H1("Matchups", className="weekText", style={"color": "#B599CE"}),
            className="weekContainer mb-2",
        ),
        html.Div(
            [
                html.Div(
                    dcc.Dropdown(
                        dropdown_options,
                        value=max_week,
                        id="matchups-dropdown",
                        placeholder="Week",
                        className="drop-down",
                        clearable=False,
                        searchable=False,
                    ),
                    className="drop-down-matchups",
                ),
                html.Div(
                    matchups_layout(matchups, max_week),
                    className="matchup",
                    id="vis-matchups",
                ),
            ],
            className="matchups",
        ),
        dcc.Interval(
            id="matchups-interval-component",
            interval=300 * 1000,  # in milliseconds
            n_intervals=0,
        ),
    ],
    className="main",
)


@dash.callback(
    Output("vis-matchups", "children"),
    Input("matchups-dropdown", "value"),
    Input("matchups-interval-component", "n_intervals"),
)
def matcups_update(value, n):
    trig_id = ctx.triggered_id
    if trig_id == "matchups-dropdown":
        if value:
            chosen_week = value
        else:
            chosen_week = max_week
        dd_matchup_layout = matchups_layout(matchups, chosen_week)
        return dd_matchup_layout
    elif trig_id == "matchups-interval-component":
        (
            t_mups,
            t_max_week,
            dropdown_options,
            # t_po_mups,
            # t_c_mups,
            # t_t_mups,
        ) = reg_season_matchups()
        time_matchup_layout = matchups_layout(t_mups, t_max_week)
        return time_matchup_layout
    else:
        return dash.no_update
