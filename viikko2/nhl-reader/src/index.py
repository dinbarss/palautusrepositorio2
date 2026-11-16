from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


SEASONS = [
    f"{year}-{str(year + 1)[-2:]}"
    for year in range(2018, 2026)
]
NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
    "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
    "NOR", "UZB", "LAT", "AUS",
]


def main():
    console = Console()
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    nationality = Prompt.ask(
        "Nationality",
        choices=NATIONALITIES,
        default="FIN",
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(
        title=f"Season {season} players from {nationality}",
        title_style="italic",
    )
    table.add_column("Player", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    console.print(table)

if __name__ == "__main__":
    main()