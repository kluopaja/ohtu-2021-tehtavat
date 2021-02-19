from player import Player
import requests
class PlayerReader:
    """Class for reading player data.

        Reads player data from `url` provided in the constructor.

        List of Player object constructed from the player data
        can be queried by the `get_player`.
    """
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []
        for player_dict in response:
            new_player = Player(name=player_dict['name'],
                    nationality=player_dict['nationality'],
                    assists=player_dict['assists'],
                    goals=player_dict['goals'],
                    penalties=player_dict['penalties'],
                    team=player_dict['team'],
                    games=player_dict['games'])
            players.append(new_player)

        return players
