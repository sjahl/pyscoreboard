from textual.app import App, ComposeResult
from textual.containers import Horizontal, Grid
from textual.widget import Widget
from textual.widgets import Footer, Header, Static, Button

from .app import default_league
from .scoreboard import fetch_scoreboard


class ScoreDisplay(Widget):
    """A widget to display a sports score"""

    DEFAULT_CSS = """
    ScoreDisplay {
        height: auto;
        padding: 1;
        border: solid blue;
    }

    ScoreDisplay Static {
        text-align: center;
        width: 100%;
    }
    """

    def __init__(self, score: str, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def compose(self) -> ComposeResult:
        yield Static(self.score)


class SportsMenu(Horizontal):
    """A button menu for selecting sports"""

    DEFAULT_CSS = """
    SportsMenu {
        height: 5;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="sports"):
            yield Button("Football", id="football", variant="success")
            yield Button("Soccer", id="soccer", variant="success")
            yield Button("Basketball", id="basketball", variant="success")


class Scoreboard(Grid):
    """A scoreboard widget"""

    DEFAULT_CSS = """
    Scoreboard {
        layout: grid;
        grid-size: 3;
        grid-rows: 1fr;
        grid-columns: 1fr;
        grid-gutter: 1;
    }
    """

    def __init__(self, sport: str = "football", league: str = "nfl", **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.league = league

    def _fetch_scores(self):
        scores = fetch_scoreboard(self.sport, self.league)
        output = []
        for game in scores.events:
            output.append(ScoreDisplay(game.simple_score))

        return output

    def reload_scores(self, sport: str, league: str):
        """Reload the scoreboard with new sport/league"""
        self.sport = sport
        self.league = league

        self.remove_children()

        scores = self._fetch_scores()
        self.mount(*scores)

    def compose(self) -> ComposeResult:
        """Create child widgets of a scoreboard"""
        scoreboard = self._fetch_scores()
        for game in scoreboard:
            yield game


class ScoreboardApp(App):
    """A textual app to display sports scores"""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield SportsMenu()
        yield Scoreboard()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks"""
        button_id = event.button.id

        sport_list = ["football", "soccer", "basketball"]

        if button_id in sport_list:
            league = default_league(button_id)
            scoreboard = self.query_one(Scoreboard)
            scoreboard.reload_scores(button_id, league)

    def on_mount(self) -> None:
        """Set up the refresh timer when the app starts"""
        self.set_interval(60, self.refresh_scoreboard)

    def refresh_scoreboard(self) -> None:
        """Refresh the scoreboard with current data"""

        scoreboard = self.query_one(Scoreboard)
        scoreboard.reload_scores(scoreboard.sport, scoreboard.league)


def main():
    app = ScoreboardApp()
    app.run()
