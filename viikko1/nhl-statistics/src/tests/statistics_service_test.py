import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_finds_player_by_partial_name(self):
        player = self.stats.search("Gret")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_for_nonexistent_player(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("PHI"), [])

    def test_top_returns_best_players_in_order_of_points(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_one_returns_player_with_most_points(self):
        players = self.stats.top(1)

        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Gretzky")

    def test_top_by_points_returns_players_with_most_points(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_by_goals_returns_players_with_most_goals(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_by_assists_returns_players_with_most_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )