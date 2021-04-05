import unittest

from tennis_game import TennisGame

test_cases = [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Forty-All"),
    (4, 4, "Deuce"),

    (1, 0, "Fifteen-Love"),
    (0, 1, "Love-Fifteen"),
    (2, 0, "Thirty-Love"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player1"),
    (0, 4, "Win for player2"),

    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player1"),
    (1, 4, "Win for player2"),

    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player1"),
    (2, 4, "Win for player2"),

    (4, 3, "Advantage player1"),
    (3, 4, "Advantage player2"),
    (5, 4, "Advantage player1"),
    (4, 5, "Advantage player2"),
    (15, 14, "Advantage player1"),
    (14, 15, "Advantage player2"),

    (6, 4, "Win for player1"),
    (4, 6, "Win for player2"),
    (16, 14, "Win for player1"),
    (14, 16, "Win for player2"),
]


def play_game(p1_points, p2_points):
    game = TennisGame("player1", "player2")
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point("player1")
        if i < p2_points:
            game.won_point("player2")
    return game

def play_game_with_names(p1_points, p2_points, p1_name, p2_name):
    game = TennisGame(p1_name, p2_name)
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point(p1_name)
        if i < p2_points:
            game.won_point(p2_name)
    return game

class TestTennis(unittest.TestCase):
    def test_score(self):
        for test_case in test_cases:
            (p1_points, p2_points, score) = test_case
            game = play_game(p1_points, p2_points)
            self.assertEqual(score, game.get_score())

    def test_correct_player_point_increased_with_custom_names(self):
        assert play_game_with_names(1, 0, "maija", "ville").get_score() == "Fifteen-Love"
        assert play_game_with_names(0, 1, "teemu", "tiina").get_score() == "Love-Fifteen"

    def test_advantage_score_prints_correct_names(self):
        assert play_game_with_names(5, 4, "maija", "ville").get_score() == "Advantage maija"
        assert play_game_with_names(4, 5, "maija", "ville").get_score() == "Advantage ville"

    def test_win_score_prints_correct_names(self):
        assert play_game_with_names(6, 4, "maija", "ville").get_score() == "Win for maija"
        assert play_game_with_names(4, 6, "maija", "ville").get_score() == "Win for ville"
