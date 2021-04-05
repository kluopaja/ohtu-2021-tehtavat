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
        score = ""
        temp_score = 0

        if self._in_end_game():
            point_difference = self.player1_points - self.player2_points

            if point_difference == 0:
                score = "Deuce"
            elif point_difference == 1:
                score = "Advantage " + self.player1_name
            elif point_difference == -1:
                score = "Advantage " + self.player2_name
            elif point_difference >= 2:
                score = "Win for " + self.player1_name
            else:
                score = "Win for " + self.player2_name
        elif self.player1_points == self.player2_points:
            score = self.simple_scores[self.player1_points]  + "-All"
        else:
            score = self.simple_scores[self.player1_points] + "-"\
                  + self.simple_scores[self.player2_points]

        return score

    def _in_end_game(self):
        return max(self.player1_points, self.player2_points) >= 4
