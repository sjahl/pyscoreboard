import requests


class EventList:
    def __init__(self, events):
        self.events = events


class Event:
    def __init__(self, uid, short_name, competitors):
        self.uid = uid
        self.short_name = short_name
        self.competitors = competitors


class Competitor:
    def __init__(self, score, team, home_away):
        self.score = score
        self.team = team
        self.home_away = home_away


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

    return r.text
