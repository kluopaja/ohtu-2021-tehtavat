class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.simple_scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self._in_end_game():
            return self._get_end_game_score()
        else:
            return self._get_early_game_score()

    def _in_end_game(self):
        return max(self.player1_points, self.player2_points) >= 4

    def _get_end_game_score(self):
        point_difference = self.player1_points - self.player2_points
        if point_difference == 0:
            return "Deuce"
        elif point_difference == 1:
            return "Advantage " + self.player1_name
        elif point_difference == -1:
            return "Advantage " + self.player2_name
        elif point_difference >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def _get_early_game_score(self):
        if self.player1_points == self.player2_points:
            return self.simple_scores[self.player1_points]  + "-All"
        else:
            return self.simple_scores[self.player1_points] + "-"\
                   + self.simple_scores[self.player2_points]
