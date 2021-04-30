import unittest
from matchers import *
from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder
class TestQueryBuilder(unittest.TestCase):
    def setUp(self):
        url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
        reader = PlayerReader(url)
        self.stats = Statistics(reader)

    def test_query_builder_plays_in_at_least_and_fewer(self):
        query = QueryBuilder()
        matcher = (
            query
            .playsIn("NYR")
            .hasAtLeast(5, "goals")
            .hasFewerThan(10, "goals")
            .build()
        )
        players = self.stats.matches(matcher)
        assert len(players) == 5
        assert players[0].name == "Greg McKegg"
        assert players[4].name == "Brett Howden"

    def test_query_builder_oneOf(self):
        query = QueryBuilder()
        matcher = (
            query
                .oneOf(
                    query.playsIn("PHI")
                        .hasAtLeast(10, "assists")
                        .hasFewerThan(5, "goals")
                        .build(),
                    query.playsIn("EDM")
                        .hasAtLeast(40, "points")
                        .build()
                )
                .build()
        )
        players = self.stats.matches(matcher)
        assert len(players) == 6
        assert players[0].name == "Justin Braun"
        assert players[5].name == "Connor McDavid"
