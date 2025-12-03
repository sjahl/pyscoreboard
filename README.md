# PyScoreboard

I'm playing around with this in a few different languages, to try to get a feel for doing it the Right Way (tm) in each one. This one is Python.

Fetches and displays from the ESPN scoreboard API

## Installation

This project is managed with `uv`.

Install deps with `uv sync`

Run the main executable with `uv run pyscoreboard`

## Running

This ships with two scripts, one for a text-only CLI, and the other with a graphical / TUI interface:

- `pyscoreboard --help`
- `pyscoreboard-tui`

## Other implementations

Also exercising this in:

- [scoreboard - Golang](https://github.com/sjahl/scoreboard)
- [scors - Rust](https://github.com/sjahl/scors)
