import requests


class Team:
    def __init__(self, abbreviation, display_name, short_name):
        self._abbreviation = abbreviation
        self._display_name = display_name
        self._short_name = short_name

    @property
    def abbreviation(self):
        return self._abbreviation

    @property
    def display_name(self):
        return self._display_name

    @property
    def short_name(self):
        return self._short_name


class Competitor:
    def __init__(self, score, team, home_away):
        self.score = score
        self.team = self._parse_team(team)
        self.home_away = home_away

    @staticmethod
    def _parse_team(team: dict) -> Team:
        return Team(team["abbreviation"], team["displayName"], team["shortDisplayName"])


class Event:
    def __init__(self, uid, short_name, competitors):
        self.uid = uid
        self.short_name = short_name
        self.competitors = self._parse_competitors(competitors)

    @property
    def simple_score(self) -> str:
        home = 0
        away = 1
        if self.competitors[0].home_away != "home":
            home = 1
            away = 0

        return f"{self.competitors[home].team.abbreviation.ljust(4)} {self.competitors[home].score.ljust(3)} - {self.competitors[away].score.rjust(3)} {self.competitors[away].team.abbreviation.rjust(4)}"

    @staticmethod
    def _parse_competitors(competitors: list[dict]) -> list[Competitor]:
        return [
            Competitor(
                c["score"],
                c["team"],
                c["homeAway"],
            )
            for c in competitors
        ]


class EventList:
    def __init__(self, events):
        self.events = self._parse_events(events)

    @staticmethod
    def _parse_events(events: list[dict]) -> list[Event]:
        return [
            Event(ev["uid"], ev["shortName"], ev["competitions"][0]["competitors"])
            for ev in events
        ]


class APIError(Exception):
    """For holding error responses from the API"""

    pass


def fetch_scoreboard(sport, league, date_str=None):
    """Given the sport and leage, fetch the scores from the scoreboard API"""

    payload = {"dates": date_str}

    r = requests.get(
        f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard",
        params=payload,
    )

    if r.status_code != 200:
        print(f"Req: url: {r.url}\nResponse Status: {r.status_code}")
        raise APIError("Failed to fetch scoreboard from API")

    return EventList(r.json()["events"])
