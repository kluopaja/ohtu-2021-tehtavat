import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_name_not_found(self):
        self.assertIsNone(self.statistics.search("lol"))
        self.assertIsNone(self.statistics.search("asKurriasdf"))

    def test_search_name_full_match(self):
        ans = self.statistics.search("Semenko")
        assert ans == Player("Semenko", "EDM", 4, 12)

        ans = self.statistics.search("Gretzky")
        assert ans == Player("Gretzky", "EDM", 35, 89)

    def test_search_name_partial_match(self):
        ans = self.statistics.search("u")
        assert ans == Player("Lemieux", "PIT", 45, 54)

        ans = self.statistics.search("zerman")
        assert ans == Player("Yzerman", "DET", 42, 56)

    def test_top_scorers_not_positive(self):
        assert self.statistics.top_scorers(-2) == []
        assert self.statistics.top_scorers(0) == []

    def test_top_scorers_positive(self):
        ans = [Player("Gretzky", "EDM", 35, 89),
               Player("Lemieux", "PIT", 45, 54)]
        assert self.statistics.top_scorers(1) == ans[0:1]
        assert self.statistics.top_scorers(2) == ans
