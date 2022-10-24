import dash
from dash import html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                "Bylaws",
                                className="text-left",
                                style={"color": "#CBB677"},
                            ),
                        )
                    ],
                    justify="left",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H3(
                                "Established 2012 - Current Year 2022",
                                className="text-left",
                                style={"color": "#CBB677"},
                            ),
                            className="mb-5",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H4(
                                                children="[Article 1.0] - League Overview",
                                                className="text-left",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        Welcome to the prestigious Men of Madison Fantasy Football League (MoM FFL). 
                                        This is a 10-Team league formed in 2012 by the gentlemen of Phi Epsilon Kappa - Delta Gamma Chapter from James Madison University. 
                                        This is considered a money league and all owners are expected to pay their league dues before the draft begins. 
                                        This league is extremely competitive and will be treated as such. 
                                        There are rules, which are decided based on a voting system. 
                                        All changes to articles will require a majority vote (greater than 50%) by all owners. 
                                        This is an evolving document and will change as the league changes.
                                        """,
                                        style={"padding": "10px"}
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 1.1] - Executive Committee",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The commissioner and co-commissioner will be elected by a majority vote from owners within the league. 
                                        Current commish/co-commish are listed:
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Commission: Tim Cuddeback"),
                                            html.Li("Co-Commissioner: Peter Billups"),
                                            html.Li(["Treasurer: ", html.A("Pat America", href="@Patrick-Amerena")]),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 1.2] - Voting",
                                                className="text-right",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        A majority vote of > 50% will be required for a vote to pass. 
                                        Voting during the season on changes will need to be unanimous. 
                                        Voting will be made on all changes to the league including, but not limited to:
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Bylaws"),
                                            html.Li("Scoring"),
                                            html.Li("League Members/removal of a member"),
                                            html.Li("Draft day/time"),
                                            html.Li("Draft location - if determined"),
                                            html.Li("League dues"),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 1.3] - Dues",
                                                className="text-right",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        This is a pay-for-league. 
                                        All dues should be collected by Pat by the date of the draft. 
                                        If dues are not in, owners are subject to removal or punishment as decided on by a vote through the league. 
                                        Current dues are:
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li(html.B("$100")),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H6(
                                                children="[Article 1.3.1] - Prize Money",
                                                className="text-right",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        Prize money will be divided up by Pat through Venmo as follows:
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("1st place = $567 (56.7%)"),
                                            html.Li("2nd place = $333 (33.3%)"),
                                            html.Li("3rd place = $100 (10%)"),
                                        ]
                                    ),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="left",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H4(
                                                children="[Article 2.0] - League Setup",
                                                className="text-left",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The MoM FFL will consist of 10 different teams, there will be no conferences. 
                                        The schedule will be selected randomly.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.1] - Draft",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        MoM FFL uses a snake draft where the person who has the 1st overall pick will have the last pick in the second round (20th pick). 
                                        Each pick in the draft will be allotted 2 minutes to determine who is selected. 
                                        The draft order will be determined by as follows: 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Names will be drawn from a hat, as names are drawn from a hat, that owner will have the ability to choose where they draft from available draft positions."),
                                            html.Li("Other options as voted on by the league"),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.2] - Playoffs",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        Playoffs will consist of 4 teams. 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The plays will start week 16 and extend 2 weeks with the championship on week 17 of the NFL season."),
                                            html.Li("The teams that are ranked #1 and #2 will play #3 and #4, with the higher seed playing the lower. "),
                                            html.Li("Teams will be selected based on the 2-point scoring system and tie breakers will be decided by most points scored in the regular season. "),
                                        ]
                                    ),
                                    html.P(
                                        """
                                        There will be a “Toilet Bowl”.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The Toilet Bowl will be formatted with week 16 having no head-to-head match-ups. "),
                                            html.Li("The top two scores from week 16 will play in week 17 for the 5th spot, the bottom two teams will play for the 9th spot, and the middle teams will play for 7th. "),
                                            html.Li("The loser of the 9th place game will be considered the loser of the toilet bowl."),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.3] - Winner",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The winner will be shipped the MoM FFL Trophy (The Kellie) to be held onto for the entire off season and until a new champion is determined. 
                                        At which point, the trophy must be shipped to the new champion.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.4] - Loser",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The loser of the regular season (determined week 15) will pay for the shipping cost of The Kellie and buy a new name engraved plate to be placed on the trophy. 
                                        The engraved plate should consist of the owner's name and year the championship was won. 
                                        The loser of the Toilet Bowl will be subjected to a “food challenge” determined by the league. 
                                        If they do not perform said food challenge, they risk being voted from the league.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("""Food challenge determined to be the “Waffle House Challenge” with the loser having to match Tim's punishment of 13 = hours + waffles"""),
                                        ]
                                    ),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="left",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H4(
                                                children="[Article 3.0] - Rosters and Lineup",
                                                className="text-left",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The MoM FFL will consist of 10 different teams, there will be no conferences. 
                                        The schedule will be selected randomly.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.1] - Draft",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        MoM FFL uses a snake draft where the person who has the 1st overall pick will have the last pick in the second round (20th pick). 
                                        Each pick in the draft will be allotted 2 minutes to determine who is selected. 
                                        The draft order will be determined by as follows: 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Names will be drawn from a hat, as names are drawn from a hat, that owner will have the ability to choose where they draft from available draft positions."),
                                            html.Li("Other options as voted on by the league"),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.2] - Playoffs",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        Playoffs will consist of 4 teams. 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The plays will start week 16 and extend 2 weeks with the championship on week 17 of the NFL season."),
                                            html.Li("The teams that are ranked #1 and #2 will play #3 and #4, with the higher seed playing the lower. "),
                                            html.Li("Teams will be selected based on the 2-point scoring system and tie breakers will be decided by most points scored in the regular season. "),
                                        ]
                                    ),
                                    html.P(
                                        """
                                        There will be a “Toilet Bowl”.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The Toilet Bowl will be formatted with week 16 having no head-to-head match-ups. "),
                                            html.Li("The top two scores from week 16 will play in week 17 for the 5th spot, the bottom two teams will play for the 9th spot, and the middle teams will play for 7th. "),
                                            html.Li("The loser of the 9th place game will be considered the loser of the toilet bowl."),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.3] - Winner",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The winner will be shipped the MoM FFL Trophy (The Kellie) to be held onto for the entire off season and until a new champion is determined. 
                                        At which point, the trophy must be shipped to the new champion.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.4] - Loser",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The loser of the regular season (determined week 15) will pay for the shipping cost of The Kellie and buy a new name engraved plate to be placed on the trophy. 
                                        The engraved plate should consist of the owner's name and year the championship was won. 
                                        The loser of the Toilet Bowl will be subjected to a “food challenge” determined by the league. 
                                        If they do not perform said food challenge, they risk being voted from the league.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("""Food challenge determined to be the “Waffle House Challenge” with the loser having to match Tim's punishment of 13 = hours + waffles"""),
                                        ]
                                    ),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="left",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        children=[
                                            html.H4(
                                                children="[Article 4.0] - Scoring",
                                                className="text-left",
                                                style={"color": "#450084"},
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The MoM FFL will consist of 10 different teams, there will be no conferences. 
                                        The schedule will be selected randomly.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.1] - Draft",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        MoM FFL uses a snake draft where the person who has the 1st overall pick will have the last pick in the second round (20th pick). 
                                        Each pick in the draft will be allotted 2 minutes to determine who is selected. 
                                        The draft order will be determined by as follows: 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("Names will be drawn from a hat, as names are drawn from a hat, that owner will have the ability to choose where they draft from available draft positions."),
                                            html.Li("Other options as voted on by the league"),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.2] - Playoffs",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        Playoffs will consist of 4 teams. 
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The plays will start week 16 and extend 2 weeks with the championship on week 17 of the NFL season."),
                                            html.Li("The teams that are ranked #1 and #2 will play #3 and #4, with the higher seed playing the lower. "),
                                            html.Li("Teams will be selected based on the 2-point scoring system and tie breakers will be decided by most points scored in the regular season. "),
                                        ]
                                    ),
                                    html.P(
                                        """
                                        There will be a “Toilet Bowl”.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("The Toilet Bowl will be formatted with week 16 having no head-to-head match-ups. "),
                                            html.Li("The top two scores from week 16 will play in week 17 for the 5th spot, the bottom two teams will play for the 9th spot, and the middle teams will play for 7th. "),
                                            html.Li("The loser of the 9th place game will be considered the loser of the toilet bowl."),
                                        ]
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.3] - Winner",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The winner will be shipped the MoM FFL Trophy (The Kellie) to be held onto for the entire off season and until a new champion is determined. 
                                        At which point, the trophy must be shipped to the new champion.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    dbc.CardHeader(
                                        children=[
                                            html.H5(
                                                children="[Article 2.4] - Loser",
                                                className="text-left",
                                            )
                                        ]
                                    ),
                                    html.P(
                                        """
                                        The loser of the regular season (determined week 15) will pay for the shipping cost of The Kellie and buy a new name engraved plate to be placed on the trophy. 
                                        The engraved plate should consist of the owner's name and year the championship was won. 
                                        The loser of the Toilet Bowl will be subjected to a “food challenge” determined by the league. 
                                        If they do not perform said food challenge, they risk being voted from the league.
                                        """,
                                        style={"padding-top": "10px", "padding-left": "10px", "padding-right": "10px"},
                                    ),
                                    html.Ul(
                                        [
                                            html.Li("""Food challenge determined to be the “Waffle House Challenge” with the loser having to match Tim's punishment of 13 = hours + waffles"""),
                                        ]
                                    ),
                                ],
                                color="dark",
                                outline=True,
                            ),
                            width="auto",
                            className="mb-4",
                        ),
                    ],
                    justify="left",
                    className="mb-5",
                ),
            ]
        )
    ]
)
