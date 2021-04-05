class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
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
                score = "Advantage player1"
            elif point_difference == -1:
                score = "Advantage player2"
            elif point_difference >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        elif self.player1_points == self.player2_points:
            if self.player1_points == 0:
                score = "Love-All"
            elif self.player1_points == 1:
                score = "Fifteen-All"
            elif self.player1_points == 2:
                score = "Thirty-All"
            else:
                score = "Forty-All"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_points
                else:
                    score += "-"
                    temp_score = self.player2_points

                if temp_score == 0:
                    score += "Love"
                elif temp_score == 1:
                    score += "Fifteen"
                elif temp_score == 2:
                    score += "Thirty"
                elif temp_score == 3:
                    score += "Forty"

        return score

    def _in_end_game(self):
        return max(self.player1_points, self.player2_points) >= 4
