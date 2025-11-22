import requests


class Competitor:
    def __init__(self, score, team, home_away):
        self.score = score
        self.team = team
        self.home_away = home_away

    def __eq__(self, other):
        return all([self.score == other.score])


class Event:
    def __init__(self, uid, short_name, competitors):
        self.uid = uid
        self.short_name = short_name
        self.competitors = self._parse_competitors(competitors)

    def simple_score(self):
        return "HOME 0   -   0 AWAY"

    @staticmethod
    def _parse_competitors(competitors: list[dict]) -> list[Competitor]:
        return [
            Competitor(
                c["score"],
                c["team"]["abbreviation"],
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
