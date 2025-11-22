import requests


class EventList:
    def __init__(self, events):
        self.events = events


class Event:
    def __init__(self, uid, short_name, competitors):
        self.uid = uid
        self.short_name = short_name
        self.competitors = competitors

    def simple_score(self):
        print("HOME 0   -   0 AWAY")


class Competitor:
    def __init__(self, score, team, home_away):
        self.score = score
        self.team = team
        self.home_away = home_away

    def __eq__(self, other):
        return all([self.score == other.score])


class APIError(Exception):
    """For holding error responses from the API"""

    pass


def parse_competitors(competitors: list[dict]) -> list[Competitor]:
    # Given competitors
    # return something like:
    # { "home": (team, score), "away": (team, score)}
    parsed = []
    for c in competitors:
        parsed.append(
            Competitor(
                c["score"],
                c["team"]["abbreviation"],
                c["homeAway"],
            )
        )
    return parsed


def parse_event(event):
    # Given event
    # Get the Competitors
    # create an Event with uid short name and competitors list
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

    return r.json()
