import scoreboard

test_event = scoreboard.Event(
    uid="s:1~l:10~e:401809303",
    short_name="LAD @ TOR",
    competitors=[
        {
            "id": "14",
            "uid": "s:1~l:10~t:14",
            "type": "team",
            "order": 0,
            "homeAway": "home",
            "winner": False,
            "team": {
                "id": "14",
                "uid": "s:1~l:10~t:14",
                "location": "Toronto",
                "name": "Blue Jays",
                "abbreviation": "TOR",
                "displayName": "Toronto Blue Jays",
                "shortDisplayName": "Blue Jays",
            },
            "score": "4",
        },
        {
            "id": "19",
            "uid": "s:1~l:10~t:19",
            "type": "team",
            "order": 1,
            "homeAway": "away",
            "team": {
                "id": "19",
                "uid": "s:1~l:10~t:19",
                "location": "Los Angeles",
                "name": "Dodgers",
                "abbreviation": "LAD",
                "displayName": "Los Angeles Dodgers",
                "shortDisplayName": "Dodgers",
            },
            "score": "5",
        },
    ],
)

assert isinstance(test_event, scoreboard.Event)
assert isinstance(test_event.competitors[0], scoreboard.Competitor)
assert test_event.competitors[0].team == "TOR"
assert test_event.competitors[1].score == "5"

assert test_event.simple_score == "TOR  4   -   5  LAD"
