import unittest
from matchers import *
from statistics import Statistics
from player_reader import PlayerReader
class TestMatchers(unittest.TestCase):
    def setUp(self):
        url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
        reader = PlayerReader(url)
        self.stats = Statistics(reader)

    def test_not_and_has_fewer_than(self):
        matcher1 = And(
            Not(HasAtLeast(1, "goals")),
            PlaysIn("NYR")
        )

        matcher2 = And(
            HasFewerThan(1, "goals"),
            PlaysIn("NYR")
        )

        assert self.stats.matches(matcher1) == self.stats.matches(matcher2)

    def test_or_1(self):
        matcher = Or(
            HasAtLeast(40, "goals"),
            HasAtLeast(60, "assists")
        )
        players = self.stats.matches(matcher)
        assert len(players) == 8
        assert players[0].name == "Mika Zibanejad"
        assert players[7].name == "Connor McDavid"

    def test_or_2(self):
        matcher = And(
            HasAtLeast(50, "points"),
            Or(
                PlaysIn("NYR"),
                PlaysIn("NYI"),
                PlaysIn("BOS")
            )
        )
        players = self.stats.matches(matcher)
        assert len(players) == 9
        assert players[0].name == "Brock Nelson"
        assert players[8].name == "David Pastrnak"
