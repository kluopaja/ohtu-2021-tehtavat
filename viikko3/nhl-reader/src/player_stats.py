class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
    def top_scorers_by_nationality(self, nationality):
        """Returns all players of nationality `nationality.

        The returned list will be ordered (decreasing) by the players' total score"""
        players = self.player_reader.get_players()
        selected_players = filter(lambda x: x.nationality == nationality, players)
        return sorted(selected_players, key = lambda x: -x.get_points())
