class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.simple_scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.tie = "Deuce"
        self.advantage = "Advantage"
        self.win = "Win for"
        self.all = "All"
        self.end_game_point_threshold = 4
        self.endgame_score_separator = " "
        self.early_game_score_separator = "-"

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self._in_end_game():
            return self._get_end_game_score()
        return self._get_early_game_score()

    def _in_end_game(self):
        return max(self.player1_points, self.player2_points) >= self.end_game_point_threshold

    def _get_end_game_score(self):
        absolute_point_difference = abs(self.player1_points - self.player2_points)
        if absolute_point_difference == 0:
            return self.tie
        if absolute_point_difference == 1:
            return self.advantage + self.endgame_score_separator + self._get_leading_player_name()
        return self.win + self.endgame_score_separator + self._get_leading_player_name()

    def _get_leading_player_name(self):
        if self.player1_points > self.player2_points:
            return self.player1_name
        return self.player2_name

    def _get_early_game_score(self):
        if self.player1_points == self.player2_points:
            return self.simple_scores[self.player1_points]  + self.early_game_score_separator + self.all
        else:
            return self.simple_scores[self.player1_points] + self.early_game_score_separator \
                   + self.simple_scores[self.player2_points]
