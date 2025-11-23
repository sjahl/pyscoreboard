from textual.app import App, ComposeResult
from textual.containers import VerticalGroup
from textual.widget import Widget
from textual.widgets import Footer, Header, Label, Static

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


class Scoreboard(VerticalGroup):
    """A scoreboard widget"""

    def _fetch_scores(self):
        scores = fetch_scoreboard("soccer", "eng.1")
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

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
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
