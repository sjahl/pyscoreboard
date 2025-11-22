import argparse

from .scoreboard import fetch_scoreboard, APIError


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sport",
        help="Fetch scores for the specified sport",
        type=str,
        default="soccer",
    )

    parser.add_argument(
        "-l",
        "--league",
        help="The league to fetch scores for",
        type=str,
    )

    parser.add_argument(
        "-d",
        "--date",
        help="Fetch scores for the specified date, in YYYMMDD, ex: 20110615",
        type=str,
    )

    args = parser.parse_args()
    return args


def default_league(sport):
    default_leagues = {
        "soccer": "eng.1",
        "baseball": "mlb",
        "hockey": "nhl",
        "football": "nfl",
        "basketball": "nba",
    }
    return default_leagues[sport]


def friendly_league_mapping(league):
    league_aliases = {
        "premier": "eng.1",
        "championship": "eng.2",
        "efl-1": "eng.3",
        "efl-2": "eng.4",
        "bundesliga": "ger.1",
        "bundesliga-2": "ger.2",
        "eredivisie": "ned.1",
        "college-football": "cfb",
        "mls": "usa.1",
        "mx": "mex.1",
        "laliga": "esp.1",
        "ligue-1": "fra.1",
    }

    if league in league_aliases.keys():
        return league_aliases[league]
    else:
        return league


def run():
    args = parse_args()
    print(f"You want to fetch scores for {args.sport}")

    if not args.league:
        lg = default_league(args.sport)
    else:
        lg = friendly_league_mapping(args.league)

    print(f"You want to fetch scores for {lg}")

    if args.date:
        print(f"You want to fetch scores for {args.date}")

    try:
        resp = fetch_scoreboard(args.sport, lg, args.date)

        print(resp)
    except APIError as e:
        print(e)
