from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Horizontal, Grid
from textual.widget import Widget
from textual.widgets import Footer, Header, Static, Button

from .scoreboard import fetch_scoreboard


class ScoreDisplay(Widget):
    """A widget to display a sports score"""

    DEFAULT_CSS = """
    ScoreDisplay {
        height: auto;
        content-align: left middle;
        padding: 1;
        border: solid blue;
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


class Scoreboard(Grid):
    """A scoreboard widget"""

    DEFAULT_CSS = """
    Scoreboard {
        layout: grid;
        grid-size: 3 4;
        grid-rows: 1fr;
        grid-columns: 1fr;
        grid-gutter: 1;
    }
    """

    def _fetch_scores(self):
        scores = fetch_scoreboard("football", "nfl")
        output = []
        for game in scores.events:
            output.append(ScoreDisplay(game.simple_score))

        return output

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


def main():
    app = ScoreboardApp()
    app.run()
