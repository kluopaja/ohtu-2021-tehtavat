#!/usr/bin/env python
from player import Player
import requests

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    print(response[0])
    pass
    
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

    
    print(players[0])

if __name__ == "__main__":
    main()
