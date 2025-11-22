import scoreboard

blue_jays = scoreboard.Competitor("4", "TOR", "home")
dodgers = scoreboard.Competitor("5", "LAD", "away")


def test_parse_competitors():
    """Should return a dict with home and away keys"""
    competitors = [
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
    ]

    parsed_competitors = scoreboard.parse_competitors(competitors)

    assert parsed_competitors == [blue_jays, dodgers]


test_parse_competitors()
