import unittest

from .scoreboard import Event, Competitor

test_event = Event(
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


class TestEvent(unittest.TestCase):
    def test_event_init(self):
        self.assertIsInstance(test_event, Event)

    def test_parse_competitors(self):
        self.assertIsInstance(test_event.competitors[0], Competitor)
        self.assertIsInstance(test_event.competitors[1], Competitor)

    def test_team_abbrev(self):
        self.assertEqual(test_event.competitors[0].team.abbreviation, "TOR")
        self.assertEqual(test_event.competitors[1].team.abbreviation, "LAD")

    def test_score_parsing(self):
        self.assertEqual(test_event.competitors[0].score, "4")
        self.assertEqual(test_event.competitors[1].score, "5")

    def test_simple_score(self):
        self.assertEqual(test_event.simple_score, "TOR  4   -   5  LAD")


if __name__ == "__main__":
    unittest.main()
