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
                                style={"color": "#B599CE"},
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
                                style={"color": "#B599CE"},
                            ),
                            className="mb-5",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
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
                                                style={"padding": "10px"},
                                            ),
                                            dbc.Accordion(
                                                [
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                The commissioner and co-commissioner will be elected by a majority vote from owners within the league. 
                                                                Current commish/co-commish are listed:
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        "Commission: Tim Cuddeback"
                                                                    ),
                                                                    html.Li(
                                                                        "Co-Commissioner: Peter Billups"
                                                                    ),
                                                                    html.Li(
                                                                        "Treasurer: Pat America"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 1.1] - Executive Committee",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                A majority vote of > 50% will be required for a vote to pass. 
                                                                Voting during the season on changes will need to be unanimous. 
                                                                Voting will be made on all changes to the league including, but not limited to:
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li("Bylaws"),
                                                                    html.Li("Scoring"),
                                                                    html.Li(
                                                                        "League Members/removal of a member"
                                                                    ),
                                                                    html.Li(
                                                                        "Draft day/time"
                                                                    ),
                                                                    html.Li(
                                                                        "Draft location - if determined"
                                                                    ),
                                                                    html.Li(
                                                                        "League dues"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 1.2] - Voting",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                This is a pay-for-league. 
                                                                All dues should be collected by Pat by the date of the draft. 
                                                                If dues are not in, owners are subject to removal or punishment as decided on by a vote through the league. 
                                                                Current dues are:
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        html.B("$100")
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 1.3] - Dues",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Prize money will be divided up by Pat through Venmo as follows:
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        "1st place = $567 (56.7%)"
                                                                    ),
                                                                    html.Li(
                                                                        "2nd place = $333 (33.3%)"
                                                                    ),
                                                                    html.Li(
                                                                        "3rd place = $100 (10%)"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 1.3.1] - Prize Money",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                ],
                                                start_collapsed=True,
                                                always_open=True,
                                            ),
                                        ],
                                        title="[Article 1.0] - League Overview",
                                        class_name="rounded", 
                                        style={"border-color": "#CBB677"}
                                    ),
                                ],
                                start_collapsed=True,
                                always_open=True,
                            ),
                            width="auto",
                            className="mb-1 rounded",
                        ),
                    ],
                    justify="left",
                    className="mb-2",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                """
                                                The MoM FFL will consist of 10 different teams, there will be no conferences. 
                                                The schedule will be selected randomly.
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            dbc.Accordion(
                                                [
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                MoM FFL uses a snake draft where the person who has the 1st overall pick will have the last pick in the second round (20th pick). 
                                                                Each pick in the draft will be allotted 2 minutes to determine who is selected. 
                                                                The draft order will be determined by as follows: 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        "Names will be drawn from a hat, as names are drawn from a hat, that owner will have the ability to choose where they draft from available draft positions."
                                                                    ),
                                                                    html.Li(
                                                                        "Other options as voted on by the league"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 2.1] - Draft",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Playoffs will consist of 4 teams. 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        "The plays will start week 16 and extend 2 weeks with the championship on week 17 of the NFL season."
                                                                    ),
                                                                    html.Li(
                                                                        "The teams that are ranked #1 and #2 will play #3 and #4, with the higher seed playing the lower. "
                                                                    ),
                                                                    html.Li(
                                                                        "Teams will be selected based on the 2-point scoring system and tie breakers will be decided by most points scored in the regular season. "
                                                                    ),
                                                                ]
                                                            ),
                                                            html.P(
                                                                """
                                                                There will be a “Toilet Bowl”.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        "The Toilet Bowl will be formatted with week 16 having no head-to-head match-ups. "
                                                                    ),
                                                                    html.Li(
                                                                        "The top two scores from week 16 will play in week 17 for the 5th spot, the bottom two teams will play for the 9th spot, and the middle teams will play for 7th. "
                                                                    ),
                                                                    html.Li(
                                                                        "The loser of the 9th place game will be considered the loser of the toilet bowl."
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 2.2] - Playoffs",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                The winner will be shipped the MoM FFL Trophy (The Kellie) to be held onto for the entire off season and until a new champion is determined. 
                                                                At which point, the trophy must be shipped to the new champion.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 2.3] - Winner",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                The loser of the regular season (determined week 15) will pay for the shipping cost of The Kellie and buy a new name engraved plate to be placed on the trophy. 
                                                                The engraved plate should consist of the owner's name and year the championship was won. 
                                                                The loser of the Toilet Bowl will be subjected to a “food challenge” determined by the league. 
                                                                If they do not perform said food challenge, they risk being voted from the league.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li(
                                                                        """Food challenge determined to be the “Waffle House Challenge” with the loser having to match Tim's punishment of 13 = hours + waffles"""
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 2.4] - Loser",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                ],
                                                start_collapsed=True,
                                                always_open=True,
                                            ),
                                        ],
                                        title="[Article 2.0] - League Setup",
                                        class_name="rounded", 
                                        style={"border-color": "#CBB677"},
                                    ),
                                ],
                                start_collapsed=True,
                                always_open=True,
                            ),
                            width="auto",
                            className="mb-1",
                        ),
                    ],
                    justify="left",
                    className="mb-2",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                """
                                                Rosters in MoM FFL will consist of 15 active NFL players on any team. 
                                                Owners are expected to take part in the draft whether in person or online. 
                                                League dues must be paid before time of draft. 
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            dbc.Accordion(
                                                [
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                There will be 16 spots on the roster, the positions of those spots will be as follows:
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.Ul(
                                                                [
                                                                    html.Li("QB = 1"),
                                                                    html.Li("RB = 2"),
                                                                    html.Li("WR = 2"),
                                                                    html.Li("TE = 1"),
                                                                    html.Li("Flex = 1"),
                                                                    html.Li("K = 1"),
                                                                    html.Li("DST = 1"),
                                                                    html.Li(
                                                                        "Bench = 6"
                                                                    ),
                                                                    html.Li(
                                                                        "Injury Reserve = 1"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        title="[Article 3.1] - Roster Spots",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Free Agency will be conducted on a first come, first served basis. 
                                                                Owners may add or drop as many players from their active rosters each week if it is not during playoffs. 
                                                                If an owner decides to drop a potential difference maker with no definitive or logical reason, as determined by a vote through the league, the player will be placed back on said team by the commish/co-commish. 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.2] - Free Agency",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Waiver wire will be determined by a Free-Agent Acquisition Budget (FAAB). 
                                                                Each owner will be granted $100 in FAAB with continual rolling list tiebreak after the draft to be used to auction players off the waiver wire. 
                                                                There will be no limit in the amount of FAAB that is spent on a player, however, spending wisely is advised or winds up losing. 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.P(
                                                                """
                                                                All unowned players will be placed on waivers at the scheduled start time of their game. 
                                                                In Game Time Waivers, players on a bye week will be placed on waivers Monday night at 5:30pm pacific time. 
                                                                Waivers will be processed on the morning of Wednesday following the Monday night football game. 
                                                                We will use the waiver rules by Yahoo Fantasy Football to guide the waiver wire. 
                                                                If there needs to be a change or there was an error in the waiver wire, there will be a vote on what is to happen.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.P(
                                                                """
                                                                Players that are dropped outside of normal waiver wire rules will be placed on waivers for a period of 1 day. 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.3] - Waiver Wire",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Waivers will work differently in the playoffs. 
                                                                When playoffs begin, only the teams competing for the coveted “Kellie” will be allowed to make claims off the waiver wire. 
                                                                Once waiver's have cleared, the other non-playoff teams will have access to free agents as normal. 
                                                                This means, if you don't make the playoffs, you can't use FAAB to make waiver claims. 
                                                                The commissioner will lock teams from making waiver claims for the two weeks of playoffs to prevent any problems.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.4] - Playoff Waiver Wire Rule",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Will be used as provided by the Yahoo system. 
                                                                If there is to be a change in the list, there will be a league vote.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.5] - Can't Cut List",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Trades are highly encouraged and will not have a maximum number. 
                                                                Trades may include multiple positions, FAAB, and fair-play standards. 
                                                                There will not be trade vetoes by the league. 
                                                                Trade deadline will be the Wednesday before week 13 of the NFL regular season starts.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.6] - Trades",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Starting line-ups must be submitted each week for each owner. 
                                                                Owner's may set their line-ups as they deem fair for each starting position. 
                                                                Owner's will not be required to field a full team if they can win without fielding a full roster. 
                                                                Once a player has played in a game, that player will be locked in and cannot be switched out for the remainder of the week. 
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.7] - Starting Line-ups",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                Each owner is expected to actively manage their team each week. 
                                                                Owners who do not submit a lineup by the start of the first Sunday NFL game will carry-over the previous week's lineup and will not be allowed to change it. 
                                                                Any additional penalties for starting a bye-week or injured player will also be assessed to a lineup that has been carried over. 
                                                                If an owner does not submit a lineup for two consecutive weeks, the executive committee will have the right to assume control of the team and manage it for the rest of the season. 
                                                                Any prize money won by a committee-run team will be distributed evenly to the other active owners in the league.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 3.8] - Active Ownership",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                ],
                                                start_collapsed=True,
                                                always_open=True,
                                            ),
                                        ],
                                        title="[Article 3.0] - Rosters and Lineup",
                                        class_name="rounded", 
                                        style={"border-color": "#CBB677"},
                                    ),
                                ],
                                start_collapsed=True,
                                always_open=True,
                            ),
                            width="auto",
                            className="mb-1",
                        ),
                    ],
                    justify="left",
                    className="mb-2",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(
                                        [
                                            html.P(
                                                """
                                                Scoring will be computed to two decimal places. 
                                                This will allow points to be awarded or deducted for every positive or negative yard and will dramatically reduce the change of a tie game. 
                                                Players are awarded fantasy points for each week that they are included in the team's starting lineup. 
                                                Players may only start at one position in any given week. 
                                                Points will be awarded for any plays that a player makes, ie: Running back throwing a touchdown pass.
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.P(
                                                """
                                                Passing:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li("Passing TD's = (4) pts"),
                                                    html.Li("Interceptions = (-1) pts"),
                                                    html.Li(
                                                        "Passing yards = (1) pt/25 yards"
                                                    ),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Rushing:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li("Rushing TD's = (6) pts"),
                                                    html.Li(
                                                        "Rushing yards = (1) pt/10 yards"
                                                    ),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Receiving:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li("Receiving TD's = (6) pts"),
                                                    html.Li(
                                                        "Receptions = (0.5) pts/1 reception"
                                                    ),
                                                    html.Li(
                                                        "Receiving yards = (1) pt/10 yards"
                                                    ),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Kick/Punt Returning:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li("Return TD's = (6) pts"),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Kicking:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li(
                                                        "Field Goals = (1) pt/10 yards"
                                                    ),
                                                    html.Li("Extra points = (1) pt"),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Other:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li(
                                                        "2-Point conversions = (2) pts"
                                                    ),
                                                    html.Li("Fumbles lost = (-2) pts"),
                                                    html.Li(
                                                        "Offensive fumble return for TD = (6) pts"
                                                    ),
                                                ]
                                            ),
                                            html.P(
                                                """
                                                Defense/Special Teams:
                                                """,
                                                style={
                                                    "padding-top": "10px",
                                                    "padding-left": "10px",
                                                    "padding-right": "10px",
                                                },
                                            ),
                                            html.Ul(
                                                [
                                                    html.Li("Pts Allowed 0 = (10) pts"),
                                                    html.Li(
                                                        "Pts Allowed 1 - 6 = (7) pts"
                                                    ),
                                                    html.Li(
                                                        "Pts Allowed 7 - 13 = (4) pts"
                                                    ),
                                                    html.Li(
                                                        "Pts Allowed 14 - 20 = (1) pts"
                                                    ),
                                                    html.Li(
                                                        "Pts Allowed 21 - 27 = (0) pts"
                                                    ),
                                                    html.Li(
                                                        "Pts Allowed 28 - 34 = (-1) pts"
                                                    ),
                                                    html.Li(
                                                        "Pts Allowed 35+ = (-4) pts"
                                                    ),
                                                    html.Li("Sack = (1) pt"),
                                                    html.Li("Interception = (2) pts"),
                                                    html.Li(
                                                        "Fumble recovery = (2) pts"
                                                    ),
                                                    html.Li("Interceptions = (-1) pts"),
                                                    html.Li("Touchdown = (6) pts"),
                                                    html.Li("Safety = (2) pts"),
                                                    html.Li("Block kick = (2) pts"),
                                                    html.Li(
                                                        "Kickoff/Punt return TD's = (6) pts"
                                                    ),
                                                    html.Li(
                                                        "Extra point return = (2) pts"
                                                    ),
                                                ]
                                            ),
                                            dbc.Accordion(
                                                [
                                                    dbc.AccordionItem(
                                                        [
                                                            html.P(
                                                                """
                                                                MoM FFBL will use a 2-point league scoring system. 
                                                                This will consist of 10 points being handed out weekly for wins and points scored. 
                                                                One point will be awarded to each owner who wins their head to head match-up week. 
                                                                One point will be awarded to the owners who score the top 5 most points in the league that week. 
                                                                Each time will only be able to score a maximum of 2 points each week and a minimum of 0. 
                                                                Points will be tracked by the commish on a spreadsheet and sent out at the conclusion of each NFL week and upon request by league members.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                            html.P(
                                                                """
                                                                Playoffs positions will be determined by the owner who scores the most weekly points. 
                                                                If there is a tie for any position, the owner with the higher regular season fantasy points scored will earn the position. 
                                                                This will also work for seeding if there is a tie for 2nd place, etc.
                                                                """,
                                                                style={
                                                                    "padding-top": "10px",
                                                                    "padding-left": "10px",
                                                                    "padding-right": "10px",
                                                                },
                                                            ),
                                                        ],
                                                        title="[Article 4.1] - 2-Point League Scoring",
                                                        class_name="rounded", 
                                                        style={"border-color": "#B599CE"},
                                                    ),
                                                ],
                                                start_collapsed=True,
                                                always_open=True,
                                            ),
                                        ],
                                        title="[Article 4.0] - Scoring",
                                        class_name="rounded", 
                                        style={"border-color": "#CBB677"},
                                    ),
                                ],
                                start_collapsed=True,
                                always_open=True,
                            ),
                            width="auto",
                            className="mb-1",
                        ),
                    ],
                    justify="left",
                    className="mb-2",
                ),
            ]
        )
    ]
)
