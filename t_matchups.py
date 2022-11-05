from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc

# from packages.db_connect import get_reg_season, get_playoffs

app = Dash(
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


matchup_layout = [
    html.Div(
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
                            "Poor Decisions 😢",
                            html.Div("Pete", className="totalProjection"),
                        ],
                        className="name",
                    ),
                    html.Div(
                        ["180.19", html.Div("110.69", className="totalProjection")],
                        className="totalPoints totalPointsR",
                    ),
                ],
                className="opponent home",
            ),
            html.Div(
                [
                    html.Div(
                        ["180.19", html.Div("110.69", className="totalProjection")],
                        className="totalPoints totalPointsL",
                    ),
                    html.Div(
                        [
                            "Fantasy Sidelines",
                            html.Div("Tim", className="totalProjection"),
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
    ),
]

matchup_page = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.Div("<", className="material-icons changeWeek"),
                    html.Span(className="spacer"),
                    html.H3("Week", className="weekText"),
                    html.Div(">", className="material-icons changeWeek"),
                    html.Span(className="spacer"),
                ],
                className="weekContainer",
            ),
            html.Div(matchup_layout, className="matchup"),
        ],
        className="matchups",
    ),
    className="main",
)


app.layout = matchup_page

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
